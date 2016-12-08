import curate.variants


def test_icgc():
    assert len(curate.variants.icgc2pb("tests/variants.tsv")) == 663
