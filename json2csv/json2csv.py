import json
import csv


def convert_json_to_csv(json_file_path, csv_file_path):
    try:
        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)

        with open(csv_file_path, "w", newline="") as csv_file:
            diagram = data["diagram"]
            csv_file.write(f"## {diagram['title']}\n")
            csv_file.write(
                "# style: shape=%shape%;fillColor=%fill%;strokeColor=%stroke%;verticalLabelPosition=bottom;\n"
            )
            for key, value in diagram["style"].items():
                csv_file.write(f"# {key}: {value}\n")
            csv_file.write("# namespace: csvimport-\n")
            csv_file.write(
                '# connect: {"from":"refs", "to":"id", "invert":true, "style":"curved=0;endArrow=none;endFill=0;dashed=1;strokeColor=#6c8ebf;"}\n'
            )
            csv_file.write("## CSV data starts below this line\n")
            csv_file.write("id,component,fill,stroke,shape,refs\n")

            writer = csv.writer(csv_file)

            # CSVデータ行の生成
            for resource in data["resources"]:
                row = [
                    resource["id"],
                    resource["component"],
                    resource["fill"],
                    resource["stroke"],
                    resource["shape"],
                    ",".join(str(ref) for ref in resource["refs"]),
                ]
                writer.writerow(row)

        print(
            f"JSON file '{json_file_path}' has been converted to CSV file '{csv_file_path}'."
        )
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    json_file_path = "./source.json"
    csv_file_path = "./dest.csv"
    convert_json_to_csv(json_file_path, csv_file_path)
