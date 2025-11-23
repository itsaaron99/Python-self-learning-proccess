class Camera:

    def __init__(self, storage_gb: float = 256.0):

        self.is_on = False
        self.mode = "photo"
        self.photos_taken = 0
        self.storage_gb_remaining = storage_gb
        print(f"Camera object created with {self.storage_gb_remaining} GB storage.")


    def turn_on(self) -> None:
        if not self.is_on:
            self.is_on = True
            print("Camera is on.")
        else:
            print("Camera is already on.")


    def turn_off(self) -> None:
        if self.is_on:
            self.is_on = False
            print("Camera is off.")
        else:
            print("Camera is already off.")


    def switch_mode(self, new_mode: str) -> None:
        if not self.is_on:
            print("Error: Camera is off. Cannot switch mode.")
            return
        
        if new_mode in ["photo", "video"]:
            self.mode = new_mode
            print(f"Mode switched to: {self.mode}")
        else:
            print(f"Error: '{new_mode}' mode is not supported.")


    def take_photo(self) -> None:
        if not self.is_on:
            print("Error: Camera is off. Cannot take photo.")
            return
        
        if self.mode != "photo":
            print(f"Error: Current mode is {self.mode}. Please switch to photo mode to take a photo.")
            return
        
        self.photos_taken += 1
        self.storage_gb_remaining -= 0.05  # Assume 50MB per pic
        print(f"Photo taken! This is photo number {self.photos_taken} today.")
        print(f"Remaining storage: {self.storage_gb_remaining:.2f} GB")


if __name__ == "__main__":
        print("--- Starting camera test ---")
        #create an object
        my_camera = Camera(storage_gb=64.0)
        
        my_camera.turn_off()      # Test turning off when already off
        my_camera.turn_on()       # Turn on
        my_camera.take_photo()    # Take a photo
        my_camera.take_photo()    # Take another photo
        my_camera.switch_mode("video") # Switch to video mode
        my_camera.take_photo()    # Try to take a photo in video mode (should fail)
        my_camera.switch_mode("photo") # Switch back to photo mode
        my_camera.take_photo()    # Take a photo successfully
        my_camera.turn_off()      # Turn off
        print("--- Test finished ---")
