# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Product(models.Model):
    product_id = models.IntegerField(blank=True, null=True)
    supplier_id = models.IntegerField(blank=True, null=True)
    manufacturer_id = models.IntegerField(blank=True, null=True)
    category_id_default = models.IntegerField(blank=True, null=True)
    category_id_erp = models.IntegerField(blank=True, null=True)
    category_name_erp = models.CharField(max_length=128, blank=True, null=True)
    menu_id = models.FloatField(blank=True, null=True)
    origin_id = models.IntegerField(blank=True, null=True)
    reference = models.CharField(max_length=50, blank=True, null=True)
    reference_id = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=128, blank=True, null=True)
    product_name_en = models.CharField(max_length=50, blank=True, null=True)
    product_deal_name = models.CharField(max_length=128, blank=True, null=True)
    product_deal_name_en = models.CharField(max_length=50, blank=True, null=True)
    top_text = models.CharField(max_length=50, blank=True, null=True)
    middle_text = models.CharField(max_length=50, blank=True, null=True)
    center_text = models.CharField(max_length=50, blank=True, null=True)
    bottom_text = models.CharField(max_length=50, blank=True, null=True)
    filter_text = models.CharField(max_length=50, blank=True, null=True)
    filter_list = models.CharField(max_length=128, blank=True, null=True)
    image_cover = models.CharField(max_length=128, blank=True, null=True)
    link_video = models.CharField(max_length=1024, blank=True, null=True)
    image_fetch = models.CharField(max_length=128, blank=True, null=True)
    image_trans = models.CharField(max_length=128, blank=True, null=True)
    is_fetch = models.IntegerField(blank=True, null=True)
    image_frame = models.CharField(max_length=64, blank=True, null=True)
    image_thumb = models.CharField(max_length=50, blank=True, null=True)
    thumb_start = models.CharField(max_length=50, blank=True, null=True)
    thumb_end = models.CharField(max_length=50, blank=True, null=True)
    thumb_width = models.IntegerField(blank=True, null=True)
    thumb_height = models.IntegerField(blank=True, null=True)
    is_legal_check = models.IntegerField(blank=True, null=True)
    description_legal = models.CharField(max_length=1024, blank=True, null=True)
    description = models.CharField(max_length=16384, blank=True, null=True)
    description_en = models.CharField(max_length=50, blank=True, null=True)
    description_short = models.CharField(max_length=2048, blank=True, null=True)
    description_short_en = models.CharField(max_length=50, blank=True, null=True)
    meta_description = models.CharField(max_length=256, blank=True, null=True)
    meta_keywords = models.CharField(max_length=256, blank=True, null=True)
    meta_title = models.CharField(max_length=128, blank=True, null=True)
    suggest_search = models.CharField(max_length=128, blank=True, null=True)
    link_rewrite = models.CharField(max_length=128, blank=True, null=True)
    full_link = models.CharField(max_length=128, blank=True, null=True)
    category_name = models.CharField(max_length=50, blank=True, null=True)
    manufacturer_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    text_price = models.CharField(max_length=50, blank=True, null=True)
    save_price = models.IntegerField(blank=True, null=True)
    fix_price = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    reduction_price = models.IntegerField(blank=True, null=True)
    reduction_percent = models.FloatField(blank=True, null=True)
    reduction_from = models.CharField(max_length=50, blank=True, null=True)
    reduction_to = models.CharField(max_length=50, blank=True, null=True)
    promotion_id = models.IntegerField(blank=True, null=True)
    promotion_no = models.CharField(max_length=50, blank=True, null=True)
    promotion_name = models.CharField(max_length=128, blank=True, null=True)
    promotion_name_en = models.CharField(max_length=50, blank=True, null=True)
    combo_id = models.IntegerField(blank=True, null=True)
    combo_name = models.CharField(max_length=128, blank=True, null=True)
    combo_name_en = models.CharField(max_length=50, blank=True, null=True)
    type_combo = models.IntegerField(blank=True, null=True)
    quantity_combo = models.IntegerField(blank=True, null=True)
    unit_combo = models.CharField(max_length=50, blank=True, null=True)
    type_discount = models.IntegerField(blank=True, null=True)
    have_gift = models.IntegerField(blank=True, null=True)
    reference_gift = models.IntegerField(blank=True, null=True)
    gift_content = models.CharField(max_length=128, blank=True, null=True)
    gift_list = models.CharField(max_length=50, blank=True, null=True)
    id_promotion_order = models.IntegerField(blank=True, null=True)
    order_amount = models.IntegerField(blank=True, null=True)
    order_content = models.CharField(max_length=50, blank=True, null=True)
    gift_order_list = models.CharField(max_length=50, blank=True, null=True)
    min_number = models.IntegerField(blank=True, null=True)
    max_number = models.IntegerField(blank=True, null=True)
    step_number = models.IntegerField(blank=True, null=True)
    deal_number = models.IntegerField(blank=True, null=True)
    date_start = models.CharField(max_length=50, blank=True, null=True)
    date_end = models.CharField(max_length=50, blank=True, null=True)
    deal_content = models.CharField(max_length=512, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    position_cate = models.IntegerField(blank=True, null=True)
    position_manu = models.IntegerField(blank=True, null=True)
    expired_position = models.CharField(max_length=50, blank=True, null=True)
    clasify_id = models.IntegerField(blank=True, null=True)
    type_group = models.IntegerField(blank=True, null=True)
    type_show = models.IntegerField(blank=True, null=True)
    type_sale = models.IntegerField(blank=True, null=True)
    trust_love = models.IntegerField(blank=True, null=True)
    comment_number = models.IntegerField(blank=True, null=True)
    is_hot = models.IntegerField(blank=True, null=True)
    is_home = models.IntegerField(blank=True, null=True)
    defect_id = models.CharField(max_length=50, blank=True, null=True)
    defect_type_id = models.IntegerField(blank=True, null=True)
    expire_defect = models.CharField(max_length=50, blank=True, null=True)
    is_online = models.IntegerField(blank=True, null=True)
    is_outstock = models.IntegerField(blank=True, null=True)
    is_legal = models.IntegerField(blank=True, null=True)
    legal_note = models.CharField(max_length=128, blank=True, null=True)
    is_cf = models.IntegerField(blank=True, null=True)
    is_feartured = models.IntegerField(blank=True, null=True)
    is_freeship = models.IntegerField(blank=True, null=True)
    is_top_category = models.IntegerField(blank=True, null=True)
    is_exclusive = models.IntegerField(blank=True, null=True)
    is_newdate = models.IntegerField(blank=True, null=True)
    is_reference = models.IntegerField(blank=True, null=True)
    table_size = models.IntegerField(blank=True, null=True)
    table_link = models.CharField(max_length=50, blank=True, null=True)
    total_sales = models.IntegerField(blank=True, null=True)
    total_buy = models.IntegerField(blank=True, null=True)
    show_rating = models.IntegerField(blank=True, null=True)
    rating_number = models.IntegerField(blank=True, null=True)
    rating_star = models.FloatField(blank=True, null=True)
    satisfy_number = models.IntegerField(blank=True, null=True)
    revenue = models.IntegerField(blank=True, null=True)
    origin_price = models.IntegerField(blank=True, null=True)
    origin_stock = models.IntegerField(blank=True, null=True)
    total_store = models.IntegerField(blank=True, null=True)
    gross_margin = models.IntegerField(blank=True, null=True)
    created_date = models.CharField(max_length=50, blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    updated_date = models.CharField(max_length=50, blank=True, null=True)
    updated_user = models.IntegerField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    date_etl = models.CharField(max_length=50, blank=True, null=True)
    actived = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class UsersUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    email = models.CharField(unique=True, max_length=255)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'users_user'


class UsersUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_groups'
        unique_together = (('user', 'group'),)


class UsersUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_user_permissions'
        unique_together = (('user', 'permission'),)
