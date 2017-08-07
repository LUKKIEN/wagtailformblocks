import pytest

from tests.factory.form import BaseFormFactory
from wagtailformblocks.blocks import FormChooserBlock, WagtailFormBlock


@pytest.mark.django_db
def test_wagtail_form_block_with_parent_context():
    form = BaseFormFactory()
    block = WagtailFormBlock()
    parent_context = {'parent_context': 1}
    ctx = block.get_context({'form': form}, parent_context=parent_context)
    assert ctx['parent_context'] == 1


@pytest.mark.django_db
def test_wagtail_form_block_without_parent_context():
    form = BaseFormFactory()
    block = WagtailFormBlock()
    ctx = block.get_context({'form': form}, parent_context=None)
    assert ctx['value']['form'].pk


@pytest.mark.django_db
def test_form_chooser_block_value_for_form():
    form = BaseFormFactory()
    block = FormChooserBlock()
    office_value = block.value_for_form(value=form)
    assert office_value == form.pk


@pytest.mark.django_db
def test_form_chooser_block_value_for_form_different_target_model():
    form = BaseFormFactory()
    block = FormChooserBlock()
    block.target_model = ()
    office_value = block.value_for_form(value=form)
    assert office_value == form


@pytest.mark.django_db
def test_form_chooser_block_value_from_form_none_value():
    block = FormChooserBlock()
    office_value = block.value_from_form(value=None)
    assert office_value is None


@pytest.mark.django_db
def test_form_chooser_block_value_from_form():
    form = BaseFormFactory()
    block = FormChooserBlock()
    office_value = block.value_from_form(value=form)
    assert office_value == form
