def main():
    # Prompts user for file name
    file_extension = input("File name: ").strip().lower().rsplit(".")
    # Match the file extension to its respective media type
    match file_extension[-1]:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")


main()
