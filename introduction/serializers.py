from rest_framework import serializers

from .models import Introduction, IntroductionComponent, IntroductionQuestion

class IntroductionQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntroductionQuestion
        fields = ('question', 'is_updated')

class IntroductionComponentSerializer(serializers.ModelSerializer):
    questions = serializers.ReadOnlyField(source='question_id.question')
    #questions = IntroductionQuestionSerializer(many=True, read_only=True)
    class Meta:
        model = IntroductionComponent
        #fields = '__all__'
        fields = ('sequence', 'questions', 'answer')

class IntroductionSerializer(serializers.ModelSerializer):
    components = IntroductionComponentSerializer(many=True, read_only=True)
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Introduction
        #fields = '__all__'
        exclude = ['created_at', 'updated_at', 'group_code']