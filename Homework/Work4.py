def get_bmi():
    height = float(input('請輸入身高120-250cm):'))
    if not (120 <= height <= 250):
        print('身高範圍輸入錯誤')
    weight = float(input('請輸入體重30-200kg):'))
    if not (30 <= weight <=200):
         print('體重範圍輸入錯誤')
    BMI = weight / ((height  / 100) **2)
    return BMI

def  get_status(BMI):
    if BMI < 18.5:
        status = '體重過輕'
    elif 18.5 <= BMI < 24:
        status = '正常範圍'
    elif 24 <= BMI < 27:
        status = '體重過重'
    elif 27 <= BMI < 30:
        status = '輕度肥胖'
    elif 30 <= BMI < 35:
        status = '中度肥胖'
    elif BMI >= 35:
        status = '重度肥胖'
    return status

def main():
    try:
        BMI = get_bmi()
        print('你的BMI為:',round(BMI,1))
        status= get_status(BMI)
        print('您的BMI為',status)
    except:
        print('輸入格式錯誤')
    finally:
        print('應用程式結束')
    
if __name__ == "__main__":
    main()  