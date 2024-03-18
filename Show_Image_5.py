import cv2

# 이미지 경로 설정
image_path = './ヨルシカ.jpg'

# 이미지 읽기
image = cv2.imread(image_path)

# 이미지가 제대로 읽어졌는지 확인
if image is not None:
    # 이미지 표시
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("이미지를 읽어오는 데 문제가 발생했습니다.")


#내 컴퓨터의 문제로 추정
#->파일명이 일본어였어서 일어난 문제.
#영문명 파일은 문제없이 작동한다.