

def main():

      def name_id(dict):
            print("Hi Joe, my name is " + dict['name'] + ' ' 'and my student ID is ' + dict['student_id'] + '.')
      def loop_pizzatoppings(datastructure,tuple):


            for t in tuple:
                  datastructure['pizza_toppings'].append(t)

            words_list = (datastructure['pizza_toppings'])
            words_list.sort()



            word = ''
            for w in words_list:
                  if (w == 'Tomatoes'):
                        word += 'and ' + w + '.'
                  else:
                        word += w + "," " "

            print("My ideal pizza has " + word)
      def loop_genre(dict):

            word2 = 'I like to watch '
            for i in range(len(dict['movies'])):
                  for x in range(len(dict['movies'][i]['genre'])):
                        if dict['movies'][i]['genre'][x] == "Crime fiction":
                              word2 += 'and ' + dict['movies'][i]['genre'][x] + 'n' '.'
                        else:
                              word2 += dict['movies'][i]['genre'][x] + ', '
            print(word2[:-2] + ' movies' + '.')

      def movie_loop(dict):
            word3 = ''
            for w in dict['movies']:
                  if w['title'] == 'The Dark Knight Rises':

                        word3 += 'and ' + w['title'] + '!'
                  else:
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
      tuple = ('Tomatoes', 'Onions', 'Napalm')



      name_id(dict)
      loop_pizzatoppings(dict,tuple)
      loop_genre(dict)
      movie_loop(dict)










main()
#