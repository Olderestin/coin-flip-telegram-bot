import random

import redis


class UserDatabase:
    """
    A class for interacting with a Redis database to store user statistics.
    """

    def __init__(
        self, redis_host: str = "localhost", redis_port: int = 6379, redis_db: int = 0
    ) -> None:
        """
        Initializes the UserDatabase instance.

        Args:
            redis_host: The hostname of the Redis server.
            redis_port: The port number of the Redis server.
            redis_db: The database index to use.
        """
        self.redis = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

    def make_flip(self, user_id: int) -> str:
        """
        Simulates a coin flip, updates user statistics, and returns the result.

        Args:
            param user_id: The ID of the user making the flip.
        Returns:
            str('heads' or 'tails').

        """

        self.redis.hincrby("user:stats", str(user_id), 1)

        result = "heads" if random.randint(0, 1) == 0 else "tails"

        if result == "heads":
            self.redis.hincrby("user:heads", str(user_id), 1)
        else:
            self.redis.hincrby("user:tails", str(user_id), 1)

        return result

    def get_stats(self, user_id: int) -> tuple[int, int, int]:
        """
        Retrieves user statistics from the database and returns it.

        Args:
            param user_id: The ID of the user.
        Returns:
            tuple(flips_count, heads_count, tails_count).
        """

        flips_count = int(str(self.redis.hget("user:stats", str(user_id))) or 0)
        heads_count = int(str(self.redis.hget("user:heads", str(user_id))) or 0)
        tails_count = int(str(self.redis.hget("user:tails", str(user_id))) or 0)
        return flips_count, heads_count, tails_count
