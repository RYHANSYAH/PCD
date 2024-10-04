import numpy as np
import imageio.v3 as image

def process_image(image_path, output_prefix):
   
    image_source = image.imread(image_path)
    
    
    if len(image_source.shape) > 3:
        print(f"Gambar {output_prefix} harus dalam mode RGB")
        return


    red_ch = image_source[:,:,0]
    green_ch = image_source[:,:,1]
    blue_ch = image_source[:,:,2]

    image_red = np.zeros_like(image_source)
    image_green = np.zeros_like(image_source)
    image_blue = np.zeros_like(image_source)

    image_red[:,:,0] = red_ch
    image_green[:,:,1] = green_ch
    image_blue[:,:,2] = blue_ch

    image.imwrite(f"{output_prefix}_R.jpg", image_red)
    image.imwrite(f"{output_prefix}_G.jpg", image_green)
    image.imwrite(f"{output_prefix}_B.jpg", image_blue)

    gray_image = np.mean(image_source, axis=2).astype(np.uint8)

    image.imwrite(f"{output_prefix}_Gray.jpg", gray_image)

    threshold_value = 128
    binary_image = np.where(gray_image > threshold_value, 255, 0).astype(np.uint8)

    image.imwrite(f"{output_prefix}_Threshold.jpg", binary_image)

    print(f"Proses untuk {output_prefix} selesai")

path_pepaya = "C:\\Users\\Administrator\\Downloads\\Daun Pepaya.jpeg"
path_singkong = "C:\\Users\\Administrator\\Downloads\\Singkong.jpg"
path_kenikir = "C:\\Users\\Administrator\\Downloads\\Kenikirr.jpg"

process_image(path_pepaya, "C:\\Users\\Administrator\\Documents\\PCD\\Daun pepaya\\Pepaya")
process_image(path_singkong, "C:\\Users\\Administrator\\Documents\\PCD\\singkong\\Singkong")
process_image(path_kenikir, "C:\\Users\\Administrator\\Documents\\PCD\\kenikir\\Kenikir")
print("Semua proses selesai")
