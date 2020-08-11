from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
import re

import logging

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.options.pipeline_options import GoogleCloudOptions

from apache_beam.io import ReadFromText
from apache_beam.transforms.combiners import CountCombineFn


class ReviewProcessingOptions(PipelineOptions):
  @classmethod
  def _add_argparse_args(cls, parser):
    parser.add_value_provider_argument('--text',
                        dest='text',
                        help='path for text to parse',
                        required = False,
    )

class CapitalizeAndOnlyKeepWordsStartingWithA(beam.DoFn):
  def process(self, line):
    upper_cased = line.upper()

    if upper_cased.startswith("A"):
      return [upper_cased]
    else:
      return []
    

def main(argv=None):
  options = PipelineOptions(flags=argv)
  processing_options = options.view_as(ReviewProcessingOptions)

  # installing packages used in process
  setup_options = options.view_as(SetupOptions)
  setup_options.setup_file = './setup.py'
  setup_options.save_main_session = False

  with beam.Pipeline(options=options) as p:
    # Read the text file[pattern] into a PCollection.
    words = (
      p # this is the start of the pipeline
      | 'Read' >> ReadFromText(processing_options.text) # this pipes the start to read the file line by line
      | 'ExtractWords' >> beam.FlatMap(lambda x: re.findall(r'[A-Za-z\']+', x)) # this pipes the lines to exctract word
    )

    # this extracts only words starting with A or a and capitalizes them 
    capitalized_a_words = (
      words
      | 'Capitalizse and only keep starting with A' >> beam.ParDo(CapitalizeAndOnlyKeepWordsStartingWithA())
    )

    # this counts the words
    counted_a_words = (
      capitalized_a_words 
      | "split into key value tuples for counting" >> beam.Map( lambda word: (word, 1) )
      | "count occurance of words" >> beam.CombinePerKey(CountCombineFn())
    )    

    counted_a_words | 'print counted A words' >> beam.Map(print)


if __name__ == '__main__':
  logging.getLogger().setLevel(logging.ERROR)
  main()