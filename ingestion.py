import pandas as pd
from db.models import get_session, Tennis

if __name__ == "__main__":
    path = '/home/priya/Desktop/2011.xls'
    data_df = pd.read_excel(path)

    session = get_session()

    for _, row in data_df.iterrows():
        session.add(
            Tennis(
                atp=row['ATP'],
                location=row['Location'],
                tournament=row['Tournament'],
            )
        )
    session.commit()