from rest_framework import serializers

from .models import Introduction, IntroductionComponent, IntroductionQuestion

class IntroductionQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntroductionQuestion
        fields = ('question', 'is_updated')

class IntroductionSimpleComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntroductionComponent
        fields = ['answer']

class IntroductionComponentSerializer(serializers.ModelSerializer):
    questions = serializers.ReadOnlyField(source='question_id.question')
    #questions = IntroductionQuestionSerializer(many=True, read_only=True)
    class Meta:
        model = IntroductionComponent
        fields = ('questions', 'answer')

class IntroductionListSerializer(serializers.ModelSerializer):
    simpleQna = serializers.SerializerMethodField()
    qna = serializers.SerializerMethodField()
    image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Introduction
        fields = ('id', 'image', 'created_at', 'updated_at', 'group_code', 'simpleQna', 'qna')
    
    def get_simpleQna(self, instance):
        qna = instance.qna.filter(is_simple_info=True).order_by('sequence')
        return IntroductionSimpleComponentSerializer(qna, many=True).data

    def get_qna(self, instance):
        qna = instance.qna.filter(is_simple_info=False).order_by('sequence')
        return IntroductionComponentSerializer(qna, many=True).data