my_data = [
    [ "Col_1"         , "Col_2"            ],
    [ "foo\nFoo\nFOO" , "1 I\n2 II\n3 III" ],
    [ "bar\nBar\nBAR" , "a A\nb B\nc C"    ],
    [ "baz\nBaz\nBAZ" , "4 $\n5 %\n6 ^"    ],

]

import csv

with open("test_csv.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(my_data)