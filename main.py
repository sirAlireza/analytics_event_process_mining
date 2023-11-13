import json

import pm4py
import pandas as pd


def main():
    df = preprocess(get_event_logs())
    num_events = len(df)
    num_cases = len(df["properties.distinct_id"].unique())
    print("Number of events: {}\nNumber of cases: {}".format(num_events, num_cases))
    event_log = pm4py.format_dataframe(df, case_id='properties.distinct_id', activity_key='event',
                                       timestamp_key='properties.time')

    start_activities = pm4py.get_start_activities(event_log)
    end_activities = pm4py.get_end_activities(event_log)
    print("Start activities: {}\nEnd activities: {}".format(start_activities, end_activities))

    # process_model = pm4py.discover_bpmn_inductive(event_log)
    # pm4py.view_bpmn(process_model)


def get_event_logs_old():
    chunk = next(pd.read_json('events.json', lines=True, chunksize=100000))
    json_struct = json.loads(chunk.to_json(orient="records"))
    df_flat = pd.json_normalize(json_struct)
    return df_flat


def get_event_logs():
    df = pd.concat(pd.read_json('events.json', lines=True, chunksize=100000), ignore_index=True)
    json_struct = json.loads(df.to_json(orient="records"))
    df_flat = pd.json_normalize(json_struct)
    print(len(df_flat))
    return df_flat


def preprocess(dataframe):
    dataframe['properties.time'] = pd.to_datetime(dataframe['properties.time'], unit="s").apply(
        lambda x: x.date())
    return dataframe


if __name__ == "__main__":
    main()
