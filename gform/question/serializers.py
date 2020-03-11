from rest_framework import serializers
from .models import *


class SingleAnsQuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleAnsQues
        fields = ['id', 'single_ans_ques_link', 'single_ans_ques']


class FileQuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileQues
        fields = ['id', 'file_ques_link', 'file_ques']


class MultiAnsQuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiAnsQues
        fields = ['id', 'multi_ans_ques_link', 'multi_ans_ques', 'options']


class CheckboxQuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckboxQues
        fields = ['id', 'checkbox_ques_link', 'checkbox_ques', 'options']


class LinearScaleQuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinearScaleQues
        fields = ['id', 'linear_scale_ques_link', 'linear_scale_ques']


class FormInfoSerializers(serializers.ModelSerializer):
    single_ans_ques = SingleAnsQuesSerializer(many=True,read_only=True)
    multi_ans_ques = MultiAnsQuesSerializer(many=True,read_only=True)
    file_ques = FileQuesSerializer(many=True,read_only=True)
    checkbox_ques_ans = CheckboxQuesSerializer(many=True,read_only=True)
    linear_scale_ans = LinearScaleQuesSerializer(many=True,read_only=True)

    class Meta:
        model = FormInfo
        fields = ['id', 'username_email', 'headline', 'summary',
                  'single_ans_ques', 'multi_ans_ques', 'file_ques', 'checkbox_ques_ans',
                  'linear_scale_ans']

    def create(self, validated_data):
        single_ans_data = validated_data.pop('single_ans_ques')
        multi_ans_data = validated_data.pop('multi_ans_ques')
        file_data = validated_data.pop('file_ques')
        checkbox_ques_data = validated_data.pop('checkbox_ques')
        linear_scale_data = validated_data.pop('linear_scale')

        temp = FormInfo.objects.create(**validated_data)
        for x in single_ans_data:
            SingleAnsQues.objects.create(single_ans_ques_link=temp, **x)

        for x in multi_ans_data:
            MultiAnsQues.objects.create(multi_ans_ques_link=temp, **x)

        for x in file_data:
            FileQues.objects.create(file_ques_link=temp, **x)

        for x in checkbox_ques_data:
            CheckboxQues.objects.create(checkbox_ques_link=temp, **x)

        for x in linear_scale_data:
            LinearScaleQues.objects.create(linear_scale_ques_link=temp, **x)

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
            temp.single_ans_ques_link = x.get('single_ans_ques_link', temp.single_ans_ques_link)
            temp.single_ans_ques = x.get('single_ans_ques', temp.single_ans_ques)
            temp.save()

        for x in multi_ans_data:
            temp = multi.pop(0)
            temp.multi_ans_ques_link = x.get('multi_ans_ques_link', temp.multi_ans_ques_link)
            temp.multi_ans_ques = x.get('multi_ans_ques', temp.multi_ans_ques)
            temp.options = x.get('options', temp.options)
            temp.save()

        for x in file_data:
            temp = file.pop(0)
            temp.file_ques_link = x.get('file_ques_link', temp.file_ques_link)
            temp.file_ques = x.get('file_ques', temp.file_ques)
            temp.save()

        for x in checkbox_ques_data:
            temp = checkbox.pop(0)
            temp.checkbox_ques_link = x.get('checkbox_ques_link', temp.checkbox_ques_link)
            temp.checkbox_ques = x.get('checkbox_ques', temp.checkbox_ques)
            temp.options = x.get('options', temp.options)
            temp.save()

        for x in linear_scale_data:
            temp = linear.pop(0)
            temp.linear_scale_ques_link = x.get('linear_scale_ques_link', temp.linear_scale_ques_link)
            temp.linear_scale_ques = x.get('linear_scale_ques', temp.linear_scale_ques)
            temp.save()

        return instance
