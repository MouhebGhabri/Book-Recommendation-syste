from flask import Flask, jsonify
import pickle
import numpy as np

popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

app = Flask(__name__)
@app.route('/')
def index():
     return jsonify({
         "book_name": list(popular_df['Book-Title'].values),
         "author": list(popular_df['Book-Author'].values),
         "image": list(popular_df['Image-URL-M'].values),
         "votes": list(popular_df['num_ratings'].astype(int).values),   
         "rating": list(popular_df['avg_rating'].astype(float).values)   
     })

@app.route('/recommend/<bookName>', methods=['GET'])
def recommend(bookName):
     try:
         index = np.where(pt.index == bookName)[0][0]
         similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

         data = []
         for i in similar_items:
             item = []
             temp_df = books[books['Book-Title'] == pt.index[i[0]]]
             item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
             item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
             item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

             data.append({
                 "title": item[0],
                 "author": item[1],
                 "image": item[2]
             })

         return jsonify({"recommendations": data})
     except IndexError:
         return jsonify({"error": f"No recommendations found for the book: {bookName}"}), 404
if __name__ == '__main__':
    app.run(debug=True,port='5555')