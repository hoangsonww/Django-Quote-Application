from django.db import models
from django.contrib.auth.models import User


class Quote(models.Model):
    CATEGORY_CHOICES = [
        ('Inspirational', 'Inspirational'),
        ('Motivational', 'Motivational'),
        ('General', 'General'),
        ('Love', 'Love'),
        ('Humor', 'Humor'),
        ('Philosophy', 'Philosophy'),
        ('Science', 'Science'),
        ('Technology', 'Technology'),
        ('Programming', 'Programming'),
        ('Business', 'Business'),
        ('Leadership', 'Leadership'),
        ('Success', 'Success'),
        ('Life', 'Life'),
        ('Friendship', 'Friendship'),
        ('Wisdom', 'Wisdom'),
        ('Education', 'Education'),
        ('Health', 'Health'),
        ('Fitness', 'Fitness'),
        ('Sports', 'Sports'),
        ('Music', 'Music'),
        ('Movies', 'Movies'),
        ('Art', 'Art'),
        ('Fashion', 'Fashion'),
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Nature', 'Nature'),
        ('Environment', 'Environment'),
        ('Politics', 'Politics'),
        ('Economics', 'Economics'),
        ('History', 'History'),
        ('Religion', 'Religion'),
        ('Spirituality', 'Spirituality'),
        ('Psychology', 'Psychology'),
        ('Self-Help', 'Self-Help'),
        ('Relationships', 'Relationships'),
        ('Parenting', 'Parenting'),
        ('Marriage', 'Marriage'),
        ('Family', 'Family'),
        ('Children', 'Children'),
        ('Teens', 'Teens'),
        ('Seniors', 'Seniors'),
        ('General', 'General'),
        ('Adventure', 'Adventure'),
        ('Animals', 'Animals'),
        ('Architecture', 'Architecture'),
        ('Books', 'Books'),
        ('Career', 'Career'),
        ('Comedy', 'Comedy'),
        ('Creativity', 'Creativity'),
        ('Culture', 'Culture'),
        ('Design', 'Design'),
        ('Dreams', 'Dreams'),
        ('Entertainment', 'Entertainment'),
        ('Finance', 'Finance'),
        ('Gardening', 'Gardening'),
        ('Happiness', 'Happiness'),
        ('Hobbies', 'Hobbies'),
        ('Home', 'Home'),
        ('Humanity', 'Humanity'),
        ('Innovation', 'Innovation'),
        ('Knowledge', 'Knowledge'),
        ('Language', 'Language'),
        ('Literature', 'Literature'),
        ('Mindfulness', 'Mindfulness'),
        ('Money', 'Money'),
        ('Motivation', 'Motivation'),
        ('Peace', 'Peace'),
        ('Poetry', 'Poetry'),
        ('Productivity', 'Productivity'),
        ('Science Fiction', 'Science Fiction'),
        ('Social Justice', 'Social Justice'),
        ('Society', 'Society'),
        ('Sustainability', 'Sustainability'),
        ('Time', 'Time'),
        ('Work', 'Work'),
        ('Activism', 'Activism'),
        ('Aging', 'Aging'),
        ('Astronomy', 'Astronomy'),
        ('Beauty', 'Beauty'),
        ('Belief', 'Belief'),
        ('Challenge', 'Challenge'),
        ('Change', 'Change'),
        ('Communication', 'Communication'),
        ('Community', 'Community'),
        ('Compassion', 'Compassion'),
        ('Confidence', 'Confidence'),
        ('Courage', 'Courage'),
        ('Curiosity', 'Curiosity'),
        ('Dance', 'Dance'),
        ('Diversity', 'Diversity'),
        ('Empathy', 'Empathy'),
        ('Empowerment', 'Empowerment'),
        ('Equality', 'Equality'),
        ('Ethics', 'Ethics'),
        ('Exploration', 'Exploration'),
        ('Faith', 'Faith'),
        ('Fantasy', 'Fantasy'),
        ('Fear', 'Fear'),
        ('Forgiveness', 'Forgiveness'),
        ('Freedom', 'Freedom'),
        ('Gender', 'Gender'),
        ('Gratitude', 'Gratitude'),
        ('Growth', 'Growth'),
        ('Healing', 'Healing'),
        ('Hope', 'Hope'),
        ('Human Rights', 'Human Rights'),
        ('Identity', 'Identity'),
        ('Imagination', 'Imagination'),
        ('Inclusion', 'Inclusion'),
        ('Independence', 'Independence'),
        ('Individuality', 'Individuality'),
        ('Inspiration', 'Inspiration'),
        ('Integrity', 'Integrity'),
        ('Justice', 'Justice'),
        ('Kindness', 'Kindness'),
        ('Learning', 'Learning'),
        ('LGBTQ+', 'LGBTQ+'),
        ('Loneliness', 'Loneliness'),
        ('Loss', 'Loss'),
        ('Magic', 'Magic'),
        ('Meaning', 'Meaning'),
        ('Memory', 'Memory'),
        ('Mental Health', 'Mental Health'),
        ('Minimalism', 'Minimalism'),
        ('Mythology', 'Mythology'),
        ('Opportunity', 'Opportunity'),
        ('Optimism', 'Optimism'),
        ('Patience', 'Patience'),
        ('Perspective', 'Perspective'),
        ('Philanthropy', 'Philanthropy'),
        ('Photography', 'Photography'),
        ('Resilience', 'Resilience'),
        ('Respect', 'Respect'),
        ('Responsibility', 'Responsibility'),
        ('Risk', 'Risk'),
        ('Self-Acceptance', 'Self-Acceptance'),
        ('Self-Care', 'Self-Care'),
        ('Self-Discovery', 'Self-Discovery'),
        ('Self-Esteem', 'Self-Esteem'),
        ('Self-Love', 'Self-Love'),
        ('Simplicity', 'Simplicity'),
        ('Solitude', 'Solitude'),
        ('Strength', 'Strength'),
        ('Theater', 'Theater'),
        ('Trust', 'Trust'),
        ('Truth', 'Truth'),
        ('Vulnerability', 'Vulnerability'),
        ('Wellness', 'Wellness'),
        ('Wonder', 'Wonder'),
        ('Youth', 'Youth'),
        ('Achievement', 'Achievement'),
        ('Activism', 'Activism'),
        ('Adventure', 'Adventure'),
        ('Adversity', 'Adversity'),
        ('Aging', 'Aging'),
        ('Ambition', 'Ambition'),
        ('Animals', 'Animals'),
        ('Anxiety', 'Anxiety'),
        ('Architecture', 'Architecture'),
        ('Art', 'Art'),
        ('Astronomy', 'Astronomy'),
        ('Authenticity', 'Authenticity'),
        ('Beauty', 'Beauty'),
        ('Belief', 'Belief'),
        ('Books', 'Books'),
        ('Bravery', 'Bravery'),
        ('Buddhism', 'Buddhism'),
        ('Business', 'Business'),
        ('Calm', 'Calm'),
        ('Career', 'Career'),
        ('Celebration', 'Celebration'),
        ('Challenge', 'Challenge'),
        ('Change', 'Change'),
        ('Childhood', 'Childhood'),
        ('Christianity', 'Christianity'),
        ('Cinema', 'Cinema'),
        ('Comedy', 'Comedy'),
        ('Communication', 'Communication'),
        ('Community', 'Community'),
        ('Compassion', 'Compassion'),
        ('Confidence', 'Confidence'),
        ('Consciousness', 'Consciousness'),
        ('Contentment', 'Contentment'),
        ('Courage', 'Courage'),
        ('Creativity', 'Creativity'),
        ('Criticism', 'Criticism'),
        ('Culture', 'Culture'),
        ('Curiosity', 'Curiosity'),
        ('Dance', 'Dance'),
        ('Death', 'Death'),
        ('Depression', 'Depression'),
        ('Design', 'Design'),
        ('Determination', 'Determination'),
        ('Diversity', 'Diversity'),
        ('Dreams', 'Dreams'),
        ('Economics', 'Economics'),
        ('Education', 'Education'),
        ('Empathy', 'Empathy'),
        ('Empowerment', 'Empowerment'),
        ('Energy', 'Energy'),
        ('Entertainment', 'Entertainment'),
        ('Environment', 'Environment'),
        ('Equality', 'Equality'),
        ('Ethics', 'Ethics'),
        ('Exploration', 'Exploration'),
        ('Failure', 'Failure'),
        ('Faith', 'Faith'),
        ('Family', 'Family'),
        ('Fantasy', 'Fantasy'),
        ('Fashion', 'Fashion'),
        ('Fear', 'Fear'),
        ('Feminism', 'Feminism'),
        ('Film', 'Film'),
        ('Finance', 'Finance'),
        ('Fitness', 'Fitness'),
        ('Food', 'Food'),
        ('Forgiveness', 'Forgiveness'),
        ('Freedom', 'Freedom'),
        ('Friendship', 'Friendship'),
        ('Gender', 'Gender'),
        ('Gratitude', 'Gratitude'),
        ('Grief', 'Grief'),
        ('Growth', 'Growth'),
        ('Happiness', 'Happiness'),
        ('Healing', 'Healing'),
        ('Health', 'Health'),
        ('Hinduism', 'Hinduism'),
        ('History', 'History'),
        ('Hobbies', 'Hobbies'),
        ('Home', 'Home'),
        ('Honesty', 'Honesty'),
        ('Hope', 'Hope'),
        ('Humanity', 'Humanity'),
        ('Humor', 'Humor'),
        ('Identity', 'Identity'),
        ('Imagination', 'Imagination'),
        ('Inclusion', 'Inclusion'),
        ('Independence', 'Independence'),
        ('Individuality', 'Individuality'),
        ('Innovation', 'Innovation'),
        ('Inspiration', 'Inspiration'),
        ('Integrity', 'Integrity'),
        ('Islam', 'Islam'),
        ('Judaism', 'Judaism'),
        ('Justice', 'Justice'),
        ('Kindness', 'Kindness'),
        ('Knowledge', 'Knowledge'),
        ('Language', 'Language'),
        ('Leadership', 'Leadership'),
        ('Learning', 'Learning'),
        ('Life', 'Life'),
        ('Literature', 'Literature'),
        ('Loneliness', 'Loneliness'),
        ('Loss', 'Loss'),
        ('Love', 'Love'),
        ('Magic', 'Magic'),
        ('Marriage', 'Marriage'),
        ('Meaning', 'Meaning'),
        ('Memory', 'Memory'),
        ('Minimalism', 'Minimalism'),
        ('Mindfulness', 'Mindfulness'),
        ('Money', 'Money'),
        ('Motivation', 'Motivation'),
        ('Music', 'Music'),
        ('Mystery', 'Mystery'),
        ('Mythology', 'Mythology'),
        ('Nature', 'Nature'),
        ('Opportunity', 'Opportunity'),
        ('Optimism', 'Optimism'),
        ('Parenting', 'Parenting'),
        ('Patience', 'Patience'),
        ('Peace', 'Peace'),
        ('Perseverance', 'Perseverance'),
        ('Perspective', 'Perspective'),
        ('Philanthropy', 'Philanthropy'),
        ('Philosophy', 'Philosophy'),
        ('Photography', 'Photography'),
        ('Poetry', 'Poetry'),
        ('Politics', 'Politics'),
        ('Positivity', 'Positivity'),
        ('Poverty', 'Poverty'),
        ('Power', 'Power'),
        ('Productivity', 'Productivity'),
        ('Programming', 'Programming'),
        ('Psychology', 'Psychology'),
        ('Racism', 'Racism'),
        ('Relationships', 'Relationships'),
        ('Religion', 'Religion'),
        ('Resilience', 'Resilience'),
        ('Respect', 'Respect'),
        ('Responsibility', 'Responsibility'),
        ('Risk', 'Risk'),
        ('Science', 'Science'),
        ('Self-Acceptance', 'Self-Acceptance'),
        ('Self-Care', 'Self-Care'),
        ('Self-Discovery', 'Self-Discovery'),
        ('Self-Esteem', 'Self-Esteem'),
        ('Self-Love', 'Self-Love'),
        ('Sexuality', 'Sexuality'),
        ('Simplicity', 'Simplicity'),
        ('Society', 'Society'),
        ('Solitude', 'Solitude'),
        ('Spirituality', 'Spirituality'),
        ('Sports', 'Sports'),
        ('Strength', 'Strength'),
        ('Success', 'Success'),
        ('Sustainability', 'Sustainability'),
        ('Technology', 'Technology'),
        ('Teens', 'Teens'),
        ('Theater', 'Theater'),
        ('Time', 'Time'),
        ('Travel', 'Travel'),
        ('Trust', 'Trust'),
        ('Truth', 'Truth'),
        ('Vulnerability', 'Vulnerability'),
        ('War', 'War'),
        ('Wellness', 'Wellness'),
        ('Wisdom', 'Wisdom'),
        ('Wonder', 'Wonder'),
        ('Work', 'Work'),
        ('Writing', 'Writing'),
        ('Youth', 'Youth')
    ]

    text = models.TextField()
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='General')

    def __str__(self):
        return self.text


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
