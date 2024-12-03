# # from flask import Flask, jsonify
# # import pickle
# # import numpy as np

# # popular_df = pickle.load(open('popular.pkl', 'rb'))
# # pt = pickle.load(open('pt.pkl', 'rb'))
# # books = pickle.load(open('books.pkl', 'rb'))
# # similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

# # app = Flask(__name__)

# # @app.route('/')
# # def index():
# #     # Convert data to Python native types
# #     return jsonify({
# #         "book_name": list(popular_df['Book-Title'].values),
# #         "author": list(popular_df['Book-Author'].values),
# #         "image": list(popular_df['Image-URL-M'].values),
# #         "votes": list(popular_df['num_ratings'].astype(int).values),  # Convert to int
# #         "rating": list(popular_df['avg_rating'].astype(float).values)  # Convert to float
# #     })

# # @app.route('/recommend/<bookName>', methods=['GET'])
# # def recommend(bookName):
# #     try:
# #         # Check if the book exists in the dataset
# #         index = np.where(pt.index == bookName)[0][0]
# #         similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

# #         data = []
# #         for i in similar_items:
# #             item = []
# #             temp_df = books[books['Book-Title'] == pt.index[i[0]]]
# #             item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
# #             item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
# #             item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

# #             data.append({
# #                 "title": item[0],
# #                 "author": item[1],
# #                 "image": item[2]
# #             })

# #         return jsonify({"recommendations": data})
# #     except IndexError:
# #         return jsonify({"error": f"No recommendations found for the book: {bookName}"}), 404

# # if __name__ == '__main__':
# #     app.run(debug=True)
# from flask import Flask, jsonify
# import pickle
# from flask_cors import CORS
# import numpy as np

# popular_df = pickle.load(open('popular.pkl', 'rb'))
# pt = pickle.load(open('pt.pkl', 'rb'))
# books = pickle.load(open('books.pkl', 'rb'))
# similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

# app = Flask(__name__)
# CORS(app)

# # @app.route('/all')
# # def index():


# #     # Convert data to Python native types
# #     return jsonify({
# #         "book_name": list(popular_df['Book-Title'].values),
# #         "author": list(popular_df['Book-Author'].values),
# #         "image": list(popular_df['Image-URL-M'].values),
# #         "votes": list(popular_df['num_ratings'].astype(int).values),  # Convert to int
# #         "rating": list(popular_df['avg_rating'].astype(float).values)  # Convert to float
# #     })
# @app.route('/all')
# def index():
#     try:
#         # Convert all data to Python native types
#         return jsonify({
#             "book_name": list(popular_df['Book-Title'].values),
#             "author": list(popular_df['Book-Author'].values),
#             "image": list(popular_df['Image-URL-M'].values),
#             "votes": [int(v) for v in popular_df['num_ratings'].values],  # Convert each to int
#             "rating": [float(r) for r in popular_df['avg_rating'].values]  # Convert each to float
#         })
#     except Exception as e:
#         return jsonify({"error": str(e)})


# @app.route('/recommend/<bookName>', methods=['GET'])
# def recommend(bookName):
#     try:
#         # Check if the book exists in the dataset
#         index = np.where(pt.index == bookName)[0][0]
#         similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

#         data = []
#         for i in similar_items:
#             item = []
#             temp_df = books[books['Book-Title'] == pt.index[i[0]]]
#             item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
#             item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
#             item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

#             data.append({
#                 "title": item[0],
#                 "author": item[1],
#                 "image": item[2]
#             })

#         return jsonify({"recommendations": data})
#     except IndexError:
#         return jsonify({"error": f"No recommendations found for the book: {bookName}"}), 404

# if __name__ == '__main__':
#     app.run(debug=True,)


from flask import Flask, jsonify
from flask_cors import CORS
import pickle
import numpy as np

# Load the pickled data
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/all')
def index():
    try:
        # Make sure to return JSON properly
        response = {
            "book_name": list(popular_df['Book-Title'].values),
            "author": list(popular_df['Book-Author'].values),
            "image": list(popular_df['Image-URL-M'].values),
            "votes": [int(v) for v in popular_df['num_ratings'].values],
            "rating": [float(r) for r in popular_df['avg_rating'].values]
        }
        return jsonify(response)
    except Exception as e:
        # Log the error for debugging
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
