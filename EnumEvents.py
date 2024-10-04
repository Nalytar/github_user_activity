from enum import Enum
import const


class EventTypes(Enum):
	CREATE_EVENT = 'CreateEvent'
	COMMIT_COMMENT_EVENT = 'CommitCommentEvent'
	DELETE_EVENT = 'DeleteEvent'
	FORK_EVENT = 'ForkEvent'
	GOLLUM_EVENT = 'GollumEvent'
	ISSUE_COMMENT_EVENT = 'IssueCommentEvent'
	ISSUE_EVENT = 'IssueEvent'
	MEMBER_EVENT = 'MemberEvent'
	PUBLIC_EVENT = 'PublicEvent'
	PULL_REQUEST_EVENT = 'PullRequestEvent'
	PULL_REQUEST_REVIEW_EVENT = 'PullRequestReviewEvent'
	PULL_REQUEST_REVIEW_COMMENT_EVENT = 'PullRequestReviewCommentEvent'
	PULL_REQUEST_REVIEW_THREAD_EVENT = 'PullRequestReviewThreadEvent'
	PUSH_EVENT = 'PushEvent'
	RELEASE_EVENT = 'ReleaseEvent'
	SPONSORSHIP_EVENT = 'SponsorshipEvent'
	WATCH_EVENT = 'WatchEvent'

	@classmethod
	def get_string_to_print(cls, activity: dict) -> str:
		match activity[const.ACTIVITY_TYPE]:
			case EventTypes.COMMIT_COMMENT_EVENT.value:
				return f'Commit Comment in Repository {activity[const.REPO][const.NAME]}\nFile: {activity[const.PAYLOAD][const.PATH]}\nLine {activity[const.PAYLOAD][const.LINE]}'

			case EventTypes.CREATE_EVENT.value:
				return f'Created a {activity[const.PAYLOAD][const.REF_TYPE]}' + (
					f' in {activity[const.REPO][const.NAME]}' if not activity[const.PAYLOAD][
						                                                 const.REF_TYPE] == const.REPOSITORY else f' {activity[const.REPO][const.NAME]}')

			case EventTypes.DELETE_EVENT.value:
				return f'Deleted a {activity[const.PAYLOAD][const.REF_TYPE]} in {activity[const.REPO][const.NAME]}'

			case EventTypes.FORK_EVENT.value:
				return f'Forked a Repository'

			case EventTypes.GOLLUM_EVENT.value:
				return f'Created or updated a wiki-page'

			case EventTypes.ISSUE_COMMENT_EVENT.value:
				return f'{str.title(activity[const.PAYLOAD][const.ACTION])} a issue comment'

			case EventTypes.ISSUE_EVENT.value:
				return f'{str.title(activity[const.PAYLOAD][const.ACTION])} a issue'

			case EventTypes.MEMBER_EVENT.value:
				return f'{str.title(activity[const.PAYLOAD][const.ACTION])} - MemberEvent'

			case EventTypes.PUBLIC_EVENT.value:
				return f'{activity[const.REPO][const.NAME]} was made public'

			case EventTypes.PULL_REQUEST_EVENT.value:
				return f'{str.title(activity[const.PAYLOAD][const.ACTION])} a pull request'

			case EventTypes.PULL_REQUEST_REVIEW_EVENT.value:
				return f'A pull request review for {activity[const.REPO][const.NAME]} was created'

			case EventTypes.PULL_REQUEST_REVIEW_COMMENT_EVENT.value:
				return f'Commented a pull request'

			case EventTypes.PULL_REQUEST_REVIEW_THREAD_EVENT.value:
				return f'{str.title(activity[const.PAYLOAD][const.ACTION])} a pull request thread'

			case EventTypes.PUSH_EVENT.value:
				return f'Pushed {str(len(activity[const.PAYLOAD][const.COMMITS]))} commit' + ('s' if len(
					activity[const.PAYLOAD][
						const.COMMITS]) > 1 else '') + f' to {activity[const.REPO][const.NAME]} on {activity[const.PAYLOAD][const.REF]}'

			case EventTypes.RELEASE_EVENT.value:
				return f'{str.title(activity[const.PAYLOAD][const.ACTION])} a release'

			case EventTypes.SPONSORSHIP_EVENT.value:
				return f'{str.title(activity[const.PAYLOAD][const.ACTION])} sponsorship'

			case EventTypes.WATCH_EVENT.value:
				return f'{str.title(activity[const.PAYLOAD][const.ACTION])} watching {activity[const.REPO][const.NAME]}'

			case _:
				return 'New unhandled activity!'
