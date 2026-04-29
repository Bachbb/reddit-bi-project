
CREATE DATABASE reddit_bi;
USE reddit_bi;

CREATE TABLE reddit_reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    text_content TEXT,
    subreddit VARCHAR(255),
    sentiment VARCHAR(50),
    rating INT,
    review_date DATETIME
);


SELECT * FROM reddit_reviews LIMIT 10;

SELECT COUNT(*) AS total_reviews FROM reddit_reviews;


SELECT SUM(rating) AS total_rating FROM reddit_reviews;


SELECT sentiment, COUNT(*) AS count_sentiment
FROM reddit_reviews
GROUP BY sentiment;

SELECT rating, sentiment, COUNT(*) AS count_reviews
FROM reddit_reviews
GROUP BY rating, sentiment
ORDER BY rating;


SELECT YEAR(review_date) AS year, COUNT(*) AS total_reviews
FROM reddit_reviews
GROUP BY YEAR(review_date)
ORDER BY year;