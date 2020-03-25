# -*- encoding: utf-8 -*-
# Author: hushukai

import os
import json

from config import BOOK_PAGE_TAGS_FILE_H, BOOK_PAGE_IMGS_H
from config import BOOK_PAGE_TAGS_FILE_V, BOOK_PAGE_IMGS_V
from config import BOOK_PAGE_TFRECORDS_H, BOOK_PAGE_TFRECORDS_V
from config import CRNN_TEXT_LINE_TAGS_FILE_H, CRNN_TEXT_LINE_TAGS_FILE_V

from config import CTPN_BOOK_PAGE_TAGS_FILE

# from data_generator.data_conversion_crnn import convert_annotation as convert_annotation_crnn
# from data_generator.data_conversion_ctpn import convert_annotation as convert_annotation_ctpn
from segment_book_page.data_conversion import main as segment_book_page_main
from segment_mix_line.data_conversion import main as segment_mix_line_main


if __name__ == '__main__':
    # convert_annotation_crnn(src_list=[(TEXT_LINE_TAGS_FILE_H, TEXT_LINE_IMGS_H)],
    #                         dest_file=CRNN_TEXT_LINE_TAGS_FILE_H)
    # convert_annotation_crnn(src_list=[(TEXT_LINE_TAGS_FILE_V, TEXT_LINE_IMGS_V)],
    #                         dest_file=CPTN_BOOK_PAGE_TAGS_FILE)

    # convert_annotation_ctpn(img_sources=[(BOOK_PAGE_TAGS_FILE_V, BOOK_PAGE_IMGS_V)])
    # convert_annotation_ctpn(tfrecords_dir=BOOK_PAGE_TFRECORDS_V)
    
    # segment_book_page_main()
    segment_mix_line_main()
    
    print("Done !")
