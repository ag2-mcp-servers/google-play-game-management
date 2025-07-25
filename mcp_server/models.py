# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T02:11:24+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class AchievementResetMultipleForAllRequest(BaseModel):
    achievement_ids: Optional[List[str]] = Field(
        None, description='The IDs of achievements to reset.'
    )
    kind: Optional[str] = Field(
        None,
        description='Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#achievementResetMultipleForAllRequest`.',
    )


class AchievementResetResponse(BaseModel):
    currentState: Optional[str] = Field(
        None,
        description='The current state of the achievement. This is the same as the initial state of the achievement. Possible values are: - "`HIDDEN`"- Achievement is hidden. - "`REVEALED`" - Achievement is revealed. - "`UNLOCKED`" - Achievement is unlocked. ',
    )
    definitionId: Optional[str] = Field(
        None,
        description='The ID of an achievement for which player state has been updated.',
    )
    kind: Optional[str] = Field(
        None,
        description='Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#achievementResetResponse`.',
    )
    updateOccurred: Optional[bool] = Field(
        None, description='Flag to indicate if the requested update actually occurred.'
    )


class EventsResetMultipleForAllRequest(BaseModel):
    event_ids: Optional[List[str]] = Field(
        None, description='The IDs of events to reset.'
    )
    kind: Optional[str] = Field(
        None,
        description='Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#eventsResetMultipleForAllRequest`.',
    )


class GamesPlayerLevelResource(BaseModel):
    level: Optional[int] = Field(None, description='The level for the user.')
    maxExperiencePoints: Optional[str] = Field(
        None, description='The maximum experience points for this level.'
    )
    minExperiencePoints: Optional[str] = Field(
        None, description='The minimum experience points for this level.'
    )


class Name(BaseModel):
    familyName: Optional[str] = Field(
        None,
        description='The family name of this player. In some places, this is known as the last name.',
    )
    givenName: Optional[str] = Field(
        None,
        description='The given name of this player. In some places, this is known as the first name.',
    )


class PlayerScoreResetResponse(BaseModel):
    definitionId: Optional[str] = Field(
        None,
        description='The ID of an leaderboard for which player state has been updated.',
    )
    kind: Optional[str] = Field(
        None,
        description='Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#playerScoreResetResponse`.',
    )
    resetScoreTimeSpans: Optional[List[str]] = Field(
        None,
        description='The time spans of the updated score. Possible values are: - "`ALL_TIME`" - The score is an all-time score. - "`WEEKLY`" - The score is a weekly score. - "`DAILY`" - The score is a daily score. ',
    )


class ProfileSettings(BaseModel):
    kind: Optional[str] = Field(
        None,
        description='Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#profileSettings`.',
    )
    profileVisible: Optional[bool] = None


class ScoresResetMultipleForAllRequest(BaseModel):
    kind: Optional[str] = Field(
        None,
        description='Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#scoresResetMultipleForAllRequest`.',
    )
    leaderboard_ids: Optional[List[str]] = Field(
        None, description='The IDs of leaderboards to reset.'
    )


class FieldXgafv(Enum):
    field_1 = '1'
    field_2 = '2'


class Alt(Enum):
    json = 'json'
    media = 'media'
    proto = 'proto'


class AchievementResetAllResponse(BaseModel):
    kind: Optional[str] = Field(
        None,
        description='Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#achievementResetAllResponse`.',
    )
    results: Optional[List[AchievementResetResponse]] = Field(
        None, description='The achievement reset results.'
    )


class GamesPlayerExperienceInfoResource(BaseModel):
    currentExperiencePoints: Optional[str] = Field(
        None, description='The current number of experience points for the player.'
    )
    currentLevel: Optional[GamesPlayerLevelResource] = Field(
        None, description='The current level of the player.'
    )
    lastLevelUpTimestampMillis: Optional[str] = Field(
        None,
        description='The timestamp when the player was leveled up, in millis since Unix epoch UTC.',
    )
    nextLevel: Optional[GamesPlayerLevelResource] = Field(
        None,
        description='The next level of the player. If the current level is the maximum level, this should be same as the current level.',
    )


class Player(BaseModel):
    avatarImageUrl: Optional[str] = Field(
        None, description='The base URL for the image that represents the player.'
    )
    bannerUrlLandscape: Optional[str] = Field(
        None, description='The url to the landscape mode player banner image.'
    )
    bannerUrlPortrait: Optional[str] = Field(
        None, description='The url to the portrait mode player banner image.'
    )
    displayName: Optional[str] = Field(
        None, description='The name to display for the player.'
    )
    experienceInfo: Optional[GamesPlayerExperienceInfoResource] = Field(
        None,
        description='An object to represent Play Game experience information for the player.',
    )
    kind: Optional[str] = Field(
        None,
        description='Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#player`.',
    )
    name: Optional[Name] = Field(
        None,
        description="An object representation of the individual components of the player's name. For some players, these fields may not be present.",
    )
    originalPlayerId: Optional[str] = Field(
        None,
        description='The player ID that was used for this player the first time they signed into the game in question. This is only populated for calls to player.get for the requesting player, only if the player ID has subsequently changed, and only to clients that support remapping player IDs.',
    )
    playerId: Optional[str] = Field(None, description='The ID of the player.')
    profileSettings: Optional[ProfileSettings] = Field(
        None,
        description="The player's profile settings. Controls whether or not the player's profile is visible to other players.",
    )
    title: Optional[str] = Field(
        None, description="The player's title rewarded for their game activities."
    )


class PlayerScoreResetAllResponse(BaseModel):
    kind: Optional[str] = Field(
        None,
        description='Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#playerScoreResetAllResponse`.',
    )
    results: Optional[List[PlayerScoreResetResponse]] = Field(
        None, description='The leaderboard reset results.'
    )


class HiddenPlayer(BaseModel):
    hiddenTimeMillis: Optional[str] = Field(
        None, description='Output only. The time this player was hidden.'
    )
    kind: Optional[str] = Field(
        None,
        description='Output only. Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#hiddenPlayer`.',
    )
    player: Optional[Player] = Field(
        None, description='Output only. The player information.'
    )


class HiddenPlayerList(BaseModel):
    items: Optional[List[HiddenPlayer]] = Field(None, description='The players.')
    kind: Optional[str] = Field(
        None,
        description='Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#hiddenPlayerList`.',
    )
    nextPageToken: Optional[str] = Field(
        None, description='The pagination token for the next page of results.'
    )
