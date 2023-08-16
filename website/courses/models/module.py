from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from .course import Course
from ..fields import OrderField


User = get_user_model()


class Module(models.Model):
    """A model representing a module."""

    course = models.ForeignKey(Course,
                               verbose_name=_("course"),
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=50,
                             help_text=_('Enter the module title'))
    description = models.TextField(_("description"), blank=True,
                                   help_text=_(
                                       'Enter a description of the module'
                                   ))
    order = OrderField(blank=True, for_fields=['course'])
    image = models.ImageField(_("image"), upload_to='module_images/',
                              blank=True, help_text=_('Upload a .webp image'))

    class Meta:
        ordering = ['order']
        verbose_name = _('module')
        verbose_name_plural = _('modules')

    def __str__(self):
        return f'{self.order}. {self.title}'


class Content(models.Model):
    """A model representing the content of a module."""

    module = models.ForeignKey(Module,
                               verbose_name=_('module'),
                               related_name='contents',
                               on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                     verbose_name=_('content type'),
                                     on_delete=models.CASCADE,
                                     limit_choices_to={'model__in': ('text',
                                                                     'video',
                                                                     'image',
                                                                     'file')})
    object_id = models.PositiveIntegerField(_('object id'))
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']
        verbose_name = _('content')
        verbose_name_plural = _('contents')


class ItemBase(models.Model):
    """An abstract base class for content items."""

    owner = models.ForeignKey(User,
                              verbose_name=_('owner'),
                              related_name='%(class)s_related',
                              on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=250,
                             help_text=_('Enter a title'))
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Text(ItemBase):
    """A model representing text content."""

    content = models.TextField(_('content'))


class File(ItemBase):
    """A model representing text content."""

    file = models.FileField(_('file'), upload_to='files')


class Image(ItemBase):
    """A model representing text content."""

    image = models.ImageField(_('image'), upload_to='images')


class Video(ItemBase):
    """A model representing text content."""

    url = models.URLField(_('url'))