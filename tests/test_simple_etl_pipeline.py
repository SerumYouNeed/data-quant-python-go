import pytest
from pathlib import Path
from src.data_engineering.simple_etl_pipeline import run, extract, load

@pytest.fixture()
def create_df():
    """Fixture to create a DataFrame from input CSV."""
    return extract("resources/input/sales.csv")

def test_run(tmp_path):
    """Test the entire pipeline run and check if output file is created."""
    # Temporary path
    output_file = tmp_path / "low_revenue.csv"

    # Switch load function to save in tmp_path
    from src.data_engineering import simple_etl_pipeline
    original_load = simple_etl_pipeline.load
    simple_etl_pipeline.load = lambda df, _: original_load(df, output_file)

    try:
        run()
        assert output_file.exists(), "Plik nie został utworzony"
    finally:
        # Restore original load function
        simple_etl_pipeline.load = original_load

def test_extract(create_df):
    """Test the extract function."""
    df = create_df
    assert len(df.columns) == 4
    assert not df.empty, "DataFrame jest pusty"
    assert list(df.columns) == ["transaction_id", "customer", "revenue", "date"]

def test_load(create_df, tmp_path):
    """Test the load function with a temporary file."""
    output_path = tmp_path / "low_revenue.csv"
    load(create_df, output_path)
    assert output_path.exists(), "Plik nie został utworzony"
