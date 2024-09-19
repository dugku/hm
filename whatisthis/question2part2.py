import csv
import os
import ipynb.fs.full.question2 as nb
import gpxpy

def output_csv(pathDir):
    list_ofacts = []
    for i in os.listdir(pathDir):
        full_path = os.path.join(pathDir, i)

        try:
            # Call the function with the full path to create the GeoDataFrame
            dataframe, name, typeAct = nb.create_actiity_gdf(full_path)
            dateTimeThing = ''
            time_ofact = dataframe["time"].iloc[-1] - dataframe["time"].iloc[0]
            distance = dataframe["distance"].sum()


            # Check if the DataFrame is empty before accessing its rows
            if dataframe.empty:
                print(f"Warning: The DataFrame for {i} is empty.")
            else:
                # Safe to access the first row
                dateTimeThing = dataframe['time'].iloc[0]

            list_ofacts.append([
                i, name, typeAct, dateTimeThing, time_ofact, distance
            ])


        except Exception as e:
            print(f"Error processing file {i}: {e}")

        print(list_ofacts)

    with open("activities_summary.csv", "w", newline='') as f:
        columns = ["file_name", "name", "type", "date_time", "duration", "distance"]
        writer = csv.writer(f)
        # Write the header row
        writer.writerow(columns)
        # Write each row of data
        for stuff in list_ofacts:
            writer.writerow(stuff)





output_csv("C:\\Users\\iphon\\PycharmProjects\\ExamMichaelPurtle\\gpxFiles")