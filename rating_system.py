# AdTech Average Star Rating System

class RatingSystem:
    def __init__(self):
        self.ratings = []

    # Add rating (1 to 5 stars)
    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)
        else:
            print("Invalid rating. Must be between 1 and 5.")

    # Calculate average rating
    def get_average_rating(self):
        if len(self.ratings) == 0:
            return 0
        return round(sum(self.ratings) / len(self.ratings), 2)

    # Rating distribution
    def rating_distribution(self):
        dist = {i:0 for i in range(1,6)}
        for r in self.ratings:
            dist[r] += 1
        return dist


# Example Usage
system = RatingSystem()

# Sample ratings (AdTech simulation)
sample_ratings = [5,5,4,4,3,5,2,1,5,4]

for r in sample_ratings:
    system.add_rating(r)

print("Average Rating:", system.get_average_rating())
print("Distribution:", system.rating_distribution())
