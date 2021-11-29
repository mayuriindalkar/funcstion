# def voter(age):
#     if age < 18:
#         print("eligible")
#     else:
#         print("not eligible")
# voter(20)


def distance(kms):
    if kms < 20:
        print("close")
    elif kms >=20 and kms<=50:
        print("remain",kms)
    else:
        print("close",kms)
distance(20)