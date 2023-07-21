from dataclasses import dataclass

@dataclass
class DataIngestionArtificat:
    data_zip_file_path:str
    feature_store_path:str