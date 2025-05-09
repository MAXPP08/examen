import timeit
2 from fibonacci import fibonacci
3
4 def test_fibonacci () :
5 assert fibonacci (0) == 0
6 assert fibonacci (1) == 1
7 assert fibonacci (5) == 5
8 print (" Pruebas pasadas !")
9
10 if __name__ == " __main__ ":
11 test_fibonacci ()
12 time = timeit . timeit (" fibonacci (20) ",
13 setup =" from fibonacci import fibonacci ",
14 number =100)
15 print (f" Tiempo : { time :.4 f} segundos ")
