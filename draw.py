import json
import sys
import plotly.express as px
import pandas as pd

def main(filename, threshold):
  file = open(filename, 'r')
  tvalues = json.load(file)
  try:
    neg = 0
    pos = 0
    for val in tvalues:
      if (val['value'] <threshold):
        neg = neg+1
      else:
        pos = pos+1
    print(pos, neg)
    data = {'Amount': [pos, neg], 'Valoration': ['Positive', 'Negative']}
    df= pd.DataFrame(data, columns=['Amount', 'Valoration'])
    print(df)
    fig = px.pie(df, values='Amount', names='Valoration')
    fig.show()
  except Exception as exc:
    print(exc)
  finally:
    file.close() 

if __name__ == "__main__":
    filename = str(sys.argv[1])
    threshold= float(sys.argv[2])
    main(filename, threshold)