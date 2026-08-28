"""Split configured claim-simulation PDFs into single-page PDF files.

Every resulting figure PDF is also rendered to a high-resolution PNG in a
parallel ``png_claim_simulations`` folder.
"""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from pathlib import Path

import pymupdf
from pypdf import PdfReader, PdfWriter


PDF_DIRECTORY = Path(__file__).resolve().parent.parent / "images" / "claim_simulations"
PNG_DIRECTORY = PDF_DIRECTORY.parent / "png_claim_simulations"
PNG_DPI = 300

# Add or remove filenames in these two lists as the source figures change.
CLIMATE_SCENARIO_FILES = [
    "county_scatter_claim_frequency.pdf",
    "county_scatter_total_claim_amount.pdf",
    "county_variability_claim_frequency.pdf",
    "county_variability_total_claim_amount.pdf",
]

SCENARIO_HORIZON_FILES = [
    "quantile_county_changes_claim_frequency.pdf",
    "quantile_county_changes_total_claim_amount.pdf",
    "quantile_municipality_changes_claim_frequency.pdf",
    "quantile_municipality_changes_total_claim_amount.pdf",
    "quartile_county_changes_claim_frequency.pdf",
    "quartile_county_changes_total_claim_amount.pdf",
    "quartile_municipality_changes_claim_frequency.pdf",
    "quartile_municipality_changes_total_claim_amount.pdf",
]

CLIMATE_SCENARIO_SUFFIXES = ("low", "medium", "high")
SCENARIO_HORIZON_SUFFIXES = (
    "low_mid_century",
    "low_late_century",
    "medium_mid_century",
    "medium_late_century",
    "high_mid_century",
    "high_late_century",
)


def output_paths(source: Path, suffixes: Sequence[str]) -> list[Path]:
    return [source.with_name(f"{source.stem}_{suffix}.pdf") for suffix in suffixes]


def png_output_path(pdf: Path) -> Path:
    return PNG_DIRECTORY / f"{pdf.stem}.png"


def figure_pdfs(configured_files: Sequence[tuple[Path, Sequence[str]]]) -> list[Path]:
    """All single-page figure PDFs: split outputs plus unsplit PDFs in the folder."""
    sources = {source for source, _ in configured_files}
    split_outputs = {
        output
        for source, suffixes in configured_files
        for output in output_paths(source, suffixes)
    }
    existing = set(PDF_DIRECTORY.glob("*.pdf")) - sources
    return sorted(existing | split_outputs)


def validate_configuration(
    groups: Sequence[tuple[Sequence[str], Sequence[str]]], *, overwrite: bool
) -> list[tuple[Path, Sequence[str]]]:
    configured_files: list[tuple[Path, Sequence[str]]] = []
    seen_sources: set[Path] = set()
    seen_outputs: set[Path] = set()

    for filenames, suffixes in groups:
        for filename in filenames:
            source = PDF_DIRECTORY / filename
            if source in seen_sources:
                raise ValueError(f"Source is listed more than once: {source.name}")
            seen_sources.add(source)

            if not source.is_file():
                raise ValueError(f"Source PDF does not exist: {source}")

            page_count = len(PdfReader(source).pages)
            if page_count != len(suffixes):
                raise ValueError(
                    f"{source.name} has {page_count} pages, but its group defines "
                    f"{len(suffixes)} suffixes"
                )

            for output in output_paths(source, suffixes):
                if output == source:
                    raise ValueError(f"Output would overwrite its source: {source}")
                if output in seen_outputs:
                    raise ValueError(f"Output is configured more than once: {output}")
                if output.exists() and not overwrite:
                    raise ValueError(
                        f"Output already exists: {output}\n"
                        "Run with --overwrite to replace generated files."
                    )
                seen_outputs.add(output)

            configured_files.append((source, suffixes))

    for figure in figure_pdfs(configured_files):
        png_output = png_output_path(figure)
        if png_output.exists() and not overwrite:
            raise ValueError(
                f"Output already exists: {png_output}\n"
                "Run with --overwrite to replace generated files."
            )

    return configured_files


def split_pdf(source: Path, suffixes: Sequence[str]) -> None:
    reader = PdfReader(source)
    for page, output in zip(reader.pages, output_paths(source, suffixes), strict=True):
        writer = PdfWriter()
        writer.add_page(page)
        with output.open("wb") as output_file:
            writer.write(output_file)
        print(f"Created {output.relative_to(PDF_DIRECTORY.parent.parent)}")


def convert_to_png(figure: Path, *, dpi: int = PNG_DPI) -> None:
    output = png_output_path(figure)
    with pymupdf.open(figure) as document:
        document[0].get_pixmap(dpi=dpi).save(output)
    print(f"Created {output.relative_to(PDF_DIRECTORY.parent.parent)}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Split configured multi-page claim-simulation PDFs by page."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="validate the configuration and print planned output without writing files",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="replace previously generated single-page PDFs",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    groups = (
        (CLIMATE_SCENARIO_FILES, CLIMATE_SCENARIO_SUFFIXES),
        (SCENARIO_HORIZON_FILES, SCENARIO_HORIZON_SUFFIXES),
    )

    try:
        configured_files = validate_configuration(groups, overwrite=args.overwrite)
    except ValueError as error:
        raise SystemExit(f"Configuration error: {error}") from error

    figures = figure_pdfs(configured_files)

    if args.dry_run:
        for source, suffixes in configured_files:
            for output in output_paths(source, suffixes):
                print(f"Would create {output.relative_to(PDF_DIRECTORY.parent.parent)}")
        for figure in figures:
            png_output = png_output_path(figure)
            print(f"Would create {png_output.relative_to(PDF_DIRECTORY.parent.parent)}")
        print(f"Validated {len(configured_files)} source PDFs.")
        return

    for source, suffixes in configured_files:
        split_pdf(source, suffixes)

    PNG_DIRECTORY.mkdir(exist_ok=True)
    for figure in figures:
        convert_to_png(figure)


if __name__ == "__main__":
    main()
