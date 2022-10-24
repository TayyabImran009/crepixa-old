from modeltranslation.translator import translator, TranslationOptions

from .models import Testimonial


class TestimonialTranslationOptions(TranslationOptions):
    fields = ('name', 'job_description', 'review')


translator.register(Testimonial, TestimonialTranslationOptions)
