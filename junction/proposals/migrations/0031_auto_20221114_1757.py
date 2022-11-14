# Generated by Django 3.2 on 2022-11-14 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proposals', '0030_auto_20200805_2137'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalproposal',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical proposal', 'verbose_name_plural': 'historical proposals'},
        ),
        migrations.AlterModelOptions(
            name='historicalproposalsectionreviewervote',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical ProposalSectionReviewerVote', 'verbose_name_plural': 'historical ProposalSectionReviewerVotes'},
        ),
        migrations.AddField(
            model_name='historicalproposal',
            name='history_change_reason',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalproposalsectionreviewervote',
            name='history_change_reason',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproposal',
            name='author',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Primary Speaker'),
        ),
        migrations.AlterField(
            model_name='historicalproposal',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalproposal',
            name='is_first_time_speaker',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='historicalproposal',
            name='proposal_section',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='proposals.proposalsection', verbose_name='Proposal Section'),
        ),
        migrations.AlterField(
            model_name='historicalproposal',
            name='proposal_type',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='proposals.proposaltype', verbose_name='Proposal Type'),
        ),
        migrations.AlterField(
            model_name='historicalproposalsectionreviewervote',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='is_first_time_speaker',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='proposalcomment',
            name='is_spam',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]