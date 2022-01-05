from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"푸들,말티즈,포메라니안,토이푸들,불독,시바견,슈나우져,허스키,\
            셰퍼드,리트리버,요크셔테리어,핏불테리어,도베르만,진돗개,시츄,차우차우,비글,카네코르소,\
            보더콜리,비숑,아키다견,아메리칸불리,치와와,달마시안,샤페이","limit":100,"print_urls":True, "format":"jpg"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images

