from django.db import models



class ApIpCurrJobDataView(models.Model):
    empindex = models.AutoField(db_column='empIndex', primary_key=True)  # Field name made lowercase.
    employee_id = models.BigIntegerField(db_column='EMPLOYEE_ID', unique=True, blank=True, null=True)  # Field name made lowercase.
    emp_name = models.CharField(db_column='EMP_NAME', max_length=42, blank=True, null=True)  # Field name made lowercase.
    gvrmnt_start_date = models.CharField(db_column='GVRMNT_START_DATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    org_start_date = models.CharField(db_column='ORG_START_DATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    office_phone = models.CharField(db_column='OFFICE_PHONE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qual_code = models.IntegerField(db_column='QUAL_CODE', blank=True, null=True)  # Field name made lowercase.
    qual_desc = models.CharField(db_column='QUAL_DESC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qual_type = models.CharField(db_column='QUAL_TYPE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    qual_type_desc = models.CharField(db_column='QUAL_TYPE_DESC', max_length=17, blank=True, null=True)  # Field name made lowercase.
    action_code = models.IntegerField(db_column='ACTION_CODE', blank=True, null=True)  # Field name made lowercase.
    job_grade = models.CharField(db_column='JOB_GRADE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    job_no = models.IntegerField(db_column='JOB_NO', blank=True, null=True)  # Field name made lowercase.
    job_title = models.CharField(db_column='JOB_TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    job_step = models.CharField(db_column='JOB_STEP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    action_start_date = models.CharField(db_column='ACTION_START_DATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    action_text = models.CharField(db_column='ACTION_TEXT', max_length=26, blank=True, null=True)  # Field name made lowercase.
    action_no = models.IntegerField(db_column='ACTION_NO', blank=True, null=True)  # Field name made lowercase.
    action_date = models.CharField(db_column='ACTION_DATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    action_end_date = models.CharField(db_column='ACTION_END_DATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    basic_salary = models.IntegerField(db_column='BASIC_SALARY', blank=True, null=True)  # Field name made lowercase.
    transportation = models.IntegerField(db_column='TRANSPORTATION', blank=True, null=True)  # Field name made lowercase.
    grade_basic_salary = models.CharField(db_column='GRADE_BASIC_SALARY', max_length=5, blank=True, null=True)  # Field name made lowercase.
    grade_sort_no = models.CharField(db_column='GRADE_SORT_NO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    category_code = models.IntegerField(db_column='CATEGORY_CODE', blank=True, null=True)  # Field name made lowercase.
    cat_descreption = models.CharField(db_column='CAT_DESCREPTION', max_length=19, blank=True, null=True)  # Field name made lowercase.
    sex_code = models.IntegerField(db_column='SEX_CODE', blank=True, null=True)  # Field name made lowercase.
    birth_date = models.CharField(db_column='BIRTH_DATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    birth_place = models.CharField(db_column='BIRTH_PLACE', max_length=22, blank=True, null=True)  # Field name made lowercase.
    nationality = models.IntegerField(db_column='NATIONALITY', blank=True, null=True)  # Field name made lowercase.
    nat_descreption = models.CharField(db_column='NAT_DESCREPTION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    current_dept_code = models.IntegerField(db_column='CURRENT_DEPT_CODE', blank=True, null=True)  # Field name made lowercase.
    dept_name = models.CharField(db_column='DEPT_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    working_dept_code = models.CharField(db_column='WORKING_DEPT_CODE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    manager_id = models.CharField(db_column='MANAGER_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    authority_id = models.CharField(db_column='AUTHORITY_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    work_dept_name = models.CharField(db_column='WORK_DEPT_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emp_type = models.IntegerField(db_column='EMP_TYPE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ap_ip_curr_job_data_view'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

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

