import sqlite3, argparse
p=argparse.ArgumentParser()
p.add_argument('--db', default='../data/research.db')
p.add_argument('--sql', required=True)
a=p.parse_args()
con=sqlite3.connect(a.db)
con.row_factory=sqlite3.Row
for row in con.execute(a.sql): print(dict(row))
