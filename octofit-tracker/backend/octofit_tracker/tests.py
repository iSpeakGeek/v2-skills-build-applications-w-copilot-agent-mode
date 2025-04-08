from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", email="testuser@example.com", password="password")
        self.team = Team.objects.create(name="Test Team")
        self.activity = Activity.objects.create(user=self.user, activity_type="Running", duration="01:00:00")
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)
        self.workout = Workout.objects.create(name="Test Workout", description="Test Description")

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")

    def test_team_creation(self):
        self.assertEqual(self.team.name, "Test Team")

    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, "Running")

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.score, 100)

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, "Test Workout")
