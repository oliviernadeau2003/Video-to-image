# import cv2
# import os


# def convert_video_to_images(
#     video_path, output_folder, image_prefix="frame", precision=1
# ):
#     cap = cv2.VideoCapture(video_path)
#     os.makedirs(output_folder, exist_ok=True)

#     fps = cap.get(cv2.CAP_PROP_FPS)
#     frames_to_skip = int(fps) if fps > 0 else 1
#     frames_to_skip *= precision  # Multiply frames_to_skip by precision

#     count = 0

#     while True:
#         ret, frame = cap.read()

#         if not ret:
#             break

#         if count % frames_to_skip == 0:
#             image_filename = f"{image_prefix}_{count // frames_to_skip:04d}.png"
#             image_path = os.path.join(output_folder, image_filename)
#             cv2.imwrite(image_path, frame)

#         count += 1

#     cap.release()


# if __name__ == "__main__":
#     input_video_path = "clip.mp4"
#     output_images_folder = "output_images"

#     # Set the precision (number of frames to skip) - change this value as needed
#     precision_value = float(
#         input("Choose The Precision(Higher Value Give Less Precision) : ") or 1
#     )

#     convert_video_to_images(
#         input_video_path, output_images_folder, precision=precision_value
#     )

import cv2
import os


def convert_video_to_images(
    video_path, output_folder, image_prefix="frame", precision=1
):
    cap = cv2.VideoCapture(video_path)
    os.makedirs(output_folder, exist_ok=True)

    fps = cap.get(cv2.CAP_PROP_FPS)
    frames_to_skip = int(fps) if fps > 0 else 1
    frames_to_skip *= precision

    count = 1  # Start the count from 1
    image_number = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if count % frames_to_skip == 0:
            image_filename = (
                f"{image_prefix}_{image_number:04d}.png"  # Use count directly
            )
            image_path = os.path.join(output_folder, image_filename)
            cv2.imwrite(image_path, frame)
            image_number += 1

        count += 1

    cap.release()


if __name__ == "__main__":
    input_video_path = "clip.mp4"
    output_images_folder = "output_images"

    # Set the precision (number of frames to skip) - change this value as needed
    precision_value = float(
        input("Choose The Precision(Higher Value Give Less Precision [~Image/Sec~]) : ")
        or 1
    )

    convert_video_to_images(
        input_video_path, output_images_folder, precision=precision_value
    )
