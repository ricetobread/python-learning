import os,sys

class Login():
	def __init__(self,email,password):
		self.email=email
		self.password=password
		self.data= {
			"nama1kelompokxx@gmail.com":{

				"email"		: "nama1kelompokxx@gmail.com",
				"password"	: "12345",
				"role"		: "superadmin",
			},
		

			"nama2kelompokxx@gmail.com":{

				"email"		: "nama2kelompokxx@gmail.com",
				"password"	: "12345",
				"role"		: "user",
			}	

		}

		self.history={

			"nama1kelompokxx": {
				"peminjaman buku"		: {"fisika dasar","dasar komputer dan pemrograman"},
				"tanggal_pinjam"		: "dd-mm-yyyy"

			},

			"nama2kelompokxx": {
				"peminjaman buku"	: {"kalkulus", "dasar komputer dan pemrograman", "konsep jaringan komputer"},
				"tanggal_pinjam"	: "dd-mm-yyyy"
			}
		}

	def cetak(self):
		print("System login kelompok xx !")
		print(" ")
		e_mail=input("Email: ")
		sandi=input("password :")
		if e_mail==self.data["email"] and sandi==self.data["password"]:
			print("welcome!,",self.data["role"])
			print("logged in as user email :",self.data["email"])
			print("{} meminjam buku : ".format(self.data["email"],self.history["peminjaman buku"]["tanggal_pinjam"])
			input("press any key to continue...")
		else:
			print("email dan password tidak sesuai")
			print("coba lagi,okay? :)")
			input("press any key to continue...")


# def main():
# 	print("System login kelompok xx!")
# 	email=input("Email : ")
# 	password=input("password : ")
# 	if email=="nama1kelompokxx" and password=="12345":
# 		print("welcome,superadmin")
# 		print("logged in as user email : ",super().__init__(email))
# 		peminjaman=("{} meminjam buku : ".format(email))



# if __name__ == '__main__':
# 	main()