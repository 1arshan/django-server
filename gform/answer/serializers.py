from rest_framework import serializers
from .models import *


class abcSingleAnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleAns
        fields = ['id', 'single_ans_link', 'answer_link', 'single_ans']


class abcFileAnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileAns
        fields = ['id', 'file_ans', 'answer_link', 'file_ans_link']


class abcMultiAnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiAns
        fields = ['id', 'multi_ans_link', 'answer_link', 'multi_ans']


class abcCheckboxAnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckboxAns
        fields = ['id', 'check_ans_link', 'answer_link', 'checkbox_ans']


class abcLinearScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinearScaleAns
        fields = ['id', 'linear_ans_link', 'answer_link', 'linear_ans']


class AnsInfoSerializers(serializers.ModelSerializer):
    single_ans_ques41 = abcSingleAnsSerializer(many=True, read_only=True)

    # multi_ans_ques41 = abcMultiAnsSerializer(many=True, read_only=True)
    # file_ques_ans41 = abcFileAnsSerializer(many=True, read_only=True)
    # checkbox_ques_ans41 = abcCheckboxAnsSerializer(many=True, read_only=True)
    # linear_scale41 = abcLinearScaleSerializer(many=True, read_only=True)

    class Meta:
        model = AnswerInfo
        #        fields = ['id', 'username_email', 'question_link', 'single_ans_ques41', 'file_ques_ans41',
        #                  'multi_ans_ques41', 'checkbox_ques_ans41', 'linear_scale41']
        fields = '__all__'


"""
    def create(self, validated_data):
        single_ans_data = validated_data.pop('single_ans_ques')
        multi_ans_data = validated_data.pop('multi_ans_ques')
        file_data = validated_data.pop('file_ques_ans')
        checkbox_ques_data = validated_data.pop('checkbox_ques_ans')
        linear_scale_data = validated_data.pop('linear_scale')

        temp = FormInfo.objects.create(**validated_data)
        for x in single_ans_data:
            abcSingleAnsSerializer.objects.create(single_ans_ques_link=temp, **x)

        for x in multi_ans_data:
            abcMultiAnsSerializer.objects.create(multi_ans_ques_link=temp, **x)

        for x in file_data:
            abcFileAnsSerializer.objects.create(file_ques_link=temp, **x)

        for x in checkbox_ques_data:
            abcCheckboxAnsSerializer.objects.create(checkbox_ques_link=temp, **x)

        for x in linear_scale_data:
            abcLinearScaleSerializer.objects.create(linear_scale_ques_link=temp, **x)

        return temp

    def update(self, instance, validated_data):
        single_ans_data = validated_data.pop('single_ans_ques')
        multi_ans_data = validated_data.pop('multi_ans_ques')
        file_data = validated_data.pop('file_ques')
        checkbox_ques_data = validated_data.pop('checkbox_ques')
        linear_scale_data = validated_data.pop('linear_scale')

        single = instance.single_ans_ques.all()
        single = list(single)
        multi = instance.multi_ans_ques.all()
        multi = list(multi)
        file = instance.file_ques.all()
        file = list(file)
        checkbox = instance.checkbox_ques.all()
        checkbox = list(checkbox)
        linear = instance.linear_scale.all()
        linear = list(linear)

        instance.username_email = validated_data.get('username_email', instance.username_email)
        instance.save()

        for x in single_ans_data:
            temp = single.pop(0)
            temp.name = x.get('single_ans_ques', temp.single_ans_ques)
            temp.save()

        for x in multi_ans_data:
            temp = multi.pop(0)
            temp.name = x.get('multi_ans_ques', temp.multi_ans_ques)
            temp.save()

        for x in file_data:
            temp = file.pop(0)
            temp.name = x.get('file_ques', temp.file_ques)
            temp.save()

        for x in checkbox_ques_data:
            temp = checkbox.pop(0)
            temp.name = x.get('checkbox_ques', temp.checkbox_ques)
            temp.save()

        for x in linear_scale_data:
            temp = linear.pop(0)
            temp.name = x.get('linear_scale', temp.linear_scale)
            temp.save()

        return instance
"""
