

import uuid
from time import sleep
from django.core.management.base import BaseCommand
from testr.autojudge.autojudge_runner import AutoJudgeRunner
from testr.models.submission import Submission, SubmissionStatus


class Command(BaseCommand):
    help = 'Judge submissions.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--rerun',
            action='store_true',
            help='Use this option to evaluate all submissions again.')

        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Control the amount of output printed to the screen.')

        parser.add_argument(
            '--keep',
            action='store_true',
            help='Prevent deletion of files in autojudge directory.')

        parser.add_argument(
            '--sleep_time',
            type=int,
            default=2,
            help='Number of seconds autojudge will sleep when there are no submissions to evaluate.')

    def handle(self, *args, **options):
        print("\nAutojudge running.\n")

        if options['rerun']:
            Submission.objects.update(
                status=SubmissionStatus.WAITING_EVALUATION)

        while True:

            submissions = Submission.objects.filter(
                status=SubmissionStatus.WAITING_EVALUATION)

            if submissions.count() == 0:
                # print(
                #    f"No submissions without evaluation were found. Sleeping for {options['sleep_time']} seconds.")
                sleep(options['sleep_time'])
            else:
                # last is selected because by default submissions are ordered by
                # submission time, with the most recent first.
                selected_submission = submissions.first()
                AutoJudgeRunner.evaluate(
                    selected_submission, options['keep'], options['verbose'])
