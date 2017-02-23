import io
import csv
# import cStringIO
# import vcf
import ga4gh.schemas.ga4gh.variants_pb2 as ga4gh


def icgc2pb(input_stream):
    """
    Convert a single icgc somatic variant tsv file into ga4gh variant protobuf

    ICGC SSM Format: http://docs.icgc.org/submission/guide/icgc-simple-somatic-mutation-format/
    """
    output_stream = io.BytesIO()

    for index, icgc in enumerate(csv.DictReader(input_stream, delimiter="\t")):
        output_stream.write(ga4gh.Variant(
            id=index, variant_set_id=icgc["icgc_sample_id"],
            reference_name=icgc["chromosome"],
            start=icgc["chromosome_start"], end=icgc["chromosome_end"],
            reference_bases=icgc["mutated_from_allele"],
            alternate_bases=icgc["mutated_to_allele"]))

    output_stream.write(ga4gh.VariantSet(
        id=icgc["icgc_sample_id"],
        dataset_id=icgc["project_code"]))

    return output_stream


# def pb2vcf(input_stream):
#     output_stream = cStringIO.StringIO()
#     vcf_template = vcf.Reader(filename="tb.vcf.gz")
#     vcf_writer = vcf.Writer(output_stream, 'w'), vcf_template)

#     return output_stream
