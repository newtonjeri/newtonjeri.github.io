import cv2


# Functions to retrieve an image and resize it to a given size
def resize_image(file_path):
    width = int(input("Width: "))
    height = int(input("Height: "))

    # Read the image
    img = cv2.imread(file_path)
    # print img size
    print("Size: ", img.shape, "\n")
    # Resize the image
    img = cv2.resize(img, (width, height))
    cv2.imwrite(file_path, img) # Save the image
    cv2.imshow("Resized image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Main function
def main():
    file_path = "logo1.jpg"
    resize_image(file_path)


# Run proram
if __name__ == "__main__":
    main()
