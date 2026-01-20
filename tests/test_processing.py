import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(ops_mixed):
    result = filter_by_state(ops_mixed)
    assert [x["id"] for x in result] == [1, 3]


def test_filter_by_state_custom(ops_mixed):
    result = filter_by_state(ops_mixed, "CANCELED")
    assert [x["id"] for x in result] == [2]


@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 1),
        ("PENDING", 0),
    ],
)
def test_filter_by_state_param(ops_mixed, state, expected_count):
    assert len(filter_by_state(ops_mixed, state)) == expected_count


def test_sort_by_date_desc(ops_mixed):
    result = sort_by_date(ops_mixed, descending=True)
    assert [x["id"] for x in result] == [1, 3, 2]


def test_sort_by_date_asc(ops_mixed):
    result = sort_by_date(ops_mixed, descending=False)
    assert [x["id"] for x in result] == [2, 3, 1]


def test_sort_by_date_equal_dates(ops_equal_dates):
    result = sort_by_date(ops_equal_dates)
    assert [x["id"] for x in result] == [1, 2]


@pytest.mark.parametrize(
    "bad_data_fixture",
    ["ops_bad_not_a_date", "ops_bad_empty_date", "ops_bad_missing_date"],
)
def test_sort_by_date_invalid_inputs(bad_data_fixture, request):
    bad_data = request.getfixturevalue(bad_data_fixture)
    with pytest.raises(ValueError):
        sort_by_date(bad_data)
