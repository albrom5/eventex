from django.db import models
from django.shortcuts import resolve_url as r


class Speaker(models.Model):
    name = models.CharField('nome', max_length=255)
    slug = models.SlugField('slug')
    website = models.URLField('website', blank=True)
    photo = models.URLField('foto')
    description = models.TextField('descrição', blank=True)

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'


class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'
    KINDS = (
        (EMAIL, 'Email'),
        (PHONE, 'Telefone')
    )
    speaker = models.ForeignKey('Speaker', on_delete=models.CASCADE,
                                verbose_name='palestrante')
    kind = models.CharField('tipo', max_length=1, choices=KINDS)
    value = models.CharField('valor', max_length=255)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'


class Talk(models.Model):
    title = models.CharField('título', max_length=200)
    start = models.TimeField('início', blank=True, null=True)
    description = models.TextField('descrição', blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name='palestrantes',
                                      blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'palestra'
        verbose_name_plural = 'palestras'
