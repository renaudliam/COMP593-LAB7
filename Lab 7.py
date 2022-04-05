

def main():

      def name_id():
            print("Hi Joe, my name is " + dict['name'] + ' ' 'and my student ID is ' + dict['student_id'] + '.')
      def loop_pizzatoppings():
            new_tuple = ('Tomatoes', 'Onions', 'Napalm')
            for t in new_tuple:
                  dict['pizza_toppings'].append(t)
            words_list = dict['pizza_toppings']
            words_list.sort()
            word = ''
            for w in words_list:
                  word += w + "," " "
            print("My ideal pizza has " + word)
      def loop_genre():

            word2 = 'I like to watch '
            for i in range(len(dict['movies'])):
                  for x in range(len(dict['movies'][i]['genre'])):
                        word2 += dict['movies'][i]['genre'][x] + ', '
            print(word2[:-2] + ' movies' + '.')

      def movie_loop():
            word3 = ''
            for w in dict['movies']:
                  word3 += w['title'] + ', '
            print('Some of my favorites are ' + word3)


      dict = {
            'name': 'Liam',
            'student_id': '10261507',
            'pizza_toppings': [
                  'Pepperoni',
                  'Mushrooms',
                  'Peppers',

            ],

            'movies': [
                  {'title': 'Star Wars',
                  'genre': [
                  'Sci-Fi',
                  'Action',
                  'Space opera',
                  'Adventure',
                  'Fantasy',
                  ]
                  },
                  {'title': 'Deadpool',
                  'genre': [
                  'Comedy',
                  'Romance',
                  'Superhero',


                   ]
                  }
            ]
      }
      extra_movie={'title': 'The Dark Knight Rises', 'genre': ['Drama', 'Thriller', 'Crime fiction']}
      dict['movies'].append(extra_movie)




      name_id()
      loop_pizzatoppings()
      loop_genre()
      movie_loop()










main()
#