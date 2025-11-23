#tranfer main_csv.py to OOP
from collections import defaultdict
import csv
import os
import json


class RomAnalyzer:
    def __init__(self, csv_path: str, rom_type_filter: str):
        self.csv_path = csv_path
        self.rom_type_filter = rom_type_filter
        #store data from the data_csv, which has the same logic of get_data_from_csv()
        self.data_rows = None
        self.final_results = None
        print(f"RomAnalyzer initialized for '{self.rom_type_filter}' ROMs from '{os.path.basename(self.csv_path)}'.")

    def _load_data(self) -> bool:
        """This fuction is confirming if the csv file has been loaded successfully or not"""
        try:
            with open(self.csv_path, mode='r', encoding='utf-8', newline='') as csvfile:
                # DictReader automatically uses the first row as headers
                reader = csv.DictReader(csvfile)
                self.data_rows = list(reader)
                if not self.data_rows:
                    print(f"Warning: No data found in CSV file: {self.csv_path}")
                    return False
                print(f"Successfully loaded {len(self.data_rows)} rows from {os.path.basename(self.csv_path)}.")
                return True
        except FileNotFoundError:
            print(f"Error: CSV file not found at '{self.csv_path}'.")
            return False
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")
            return False

    
    def _perform_analysis(self):
        """ Initial method of transforming original funtion: analyze_roms"""
        if not self.data_rows:
            print("No data available to analyze.")
            return None
        
        rom_to_devices = defaultdict(set)
        devices_in_scope = set()

        for row in self.data_rows:
        # If a filter is set and the current row's rom_type doesn't match, skip it.
            rom_type = row.get('rom_type', '').strip()
            if self.rom_type_filter and rom_type != self.rom_type_filter:
                continue

            device = row.get('device', '').strip()
            rom_build = row.get('rom_build', '').strip()

            if not device or not rom_build:
                continue

            devices_in_scope.add(device)
            rom_to_devices[rom_build].add(device)

        if not devices_in_scope:
            print(f"No data available for analysis after filtering for type '{self.rom_type_filter}'.")
            return None

        # Goal 1: Find ROMs common to all devices in scope.
        common_roms = {
            rom
            for rom, devices in rom_to_devices.items()
            if devices == devices_in_scope
        }
        # Prepare the detailed output format as specified.
        detailed_rom_usage = {
            rom: {
                "amount": len(devices),
                "devices": sorted(list(devices)) # Sort to ensure consistent output order.
            }
            for rom, devices in rom_to_devices.items()
        }
        return common_roms, detailed_rom_usage, devices_in_scope

    def save_results_to_json(self, output_path: str):
        """ writing self.final_results to JSON """
        if not self.final_results:
            print("No results to save. Please run the .run() method first.")
            return
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(self.final_results, f, ensure_ascii=False, indent=4, sort_keys=True)
            print(f"Results have been successfully saved to: {output_path}")
        except Exception as e:
            print(f"An error occurred while writing to the JSON file: {e}")

    def run(self):
        """ Tranforming the funtion write_results_to_json in main_csv.py
            execute the proccess: load csv data -> analyze data -> output the result in json"""
        if not self._load_data():
            print("Analysis terminated due to data loading failure.")
            return
        
        analysis_result = self._perform_analysis()
        if not analysis_result:
            print("Analysis stopped as there is no valid data to process.")
            return

        common_roms, detailed_rom_usage, devices_in_scope = analysis_result

        # This is the correct place to assemble the final results
        self.final_results = {
            "analysis_metadata": {
                "source_file": os.path.basename(self.csv_path),
                "rom_type_filter": self.rom_type_filter,
                "devices_in_scope": sorted(list(devices_in_scope)),
                "total_devices_in_scope": len(devices_in_scope)
            },
            "common_roms_for_all_devices": sorted(list(common_roms)),
            "shared_roms_usage (all devices)": detailed_rom_usage
        }
        print("Analyze has been completed.")
    
def main():
    ROM_TYPE_TO_ANALYZE = 'base'
    INPUT_CSV_FILENAME = 'data.csv'
    OUTPUT_FILENAME = f'analysis_results_{ROM_TYPE_TO_ANALYZE}.json'

    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(script_dir, INPUT_CSV_FILENAME)
    output_path = os.path.join(script_dir, OUTPUT_FILENAME)
    analyzer = RomAnalyzer(csv_path=csv_file_path, rom_type_filter=ROM_TYPE_TO_ANALYZE)
    analyzer.run()
    analyzer.save_results_to_json(output_path)

if __name__ == "__main__":
    main()
