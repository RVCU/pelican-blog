Title: Network Diagram
Date: 2020-03-06
Category: tech
Tags: tech

Current network diagram as of 2020-03-06


                           .-,(  ),-.
                        .-(          )-.
                       (    internet    )
                        '-(          ).-'              .---------.
                            '-.( ).-'                 .| rpi3-01 |
                                ^                    / '---------'
                .---.           |                   /
               /   /|      .--------.    .--------./     .---------.
              .---. |------| router |----| switch .----- | rpi4-01 |
              |   | '      '--------'    '--------'\     '---------'
              |   |/                                \
              '---'                                  \ .---------.
                                                      '| rpi4-02 |
                                                       '---------'

               rpi3-01: DNS, nfs server for USB attached TB ssd
