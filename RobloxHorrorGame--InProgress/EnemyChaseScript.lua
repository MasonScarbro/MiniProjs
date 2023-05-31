local runService = game:GetService("RunService") -- Run Service sort of like unitys Update frame by frame, SEE DOCUMENTATION SAVED FOLDER
local players = game:GetService("Players") -- Players will help "get" the players in the game

local humanoid = script.Parent -- grabs the parent of the script which is humanoid
local root = humanoid.Parent.PrimaryPart --root is the humanoids parent i.e models primary part which is typically the humanoid root part

local wantedDistance = 30 --  How far he can search or should be trying to search, The value now is small testing needed
local stopDistance = 5 -- In caase we want to use this to make him stop (like if he had a kill radius instead of touching)

function findNearestPlaya()
	local playerList = players:GetPlayers()
	
	local playerNearest = nil
	local dist = nil
	local direction = nil
	
	for _, player in pairs(playerList) do -- basically a for each loop that says for each player in the list of players
		local character = player.Character 
		if character  then -- will only eggsacute if a player/character exists
			local distanceV = player.Character.HumanoidRootPart.Position - root.Position -- Distance  ''Vector'' equals the distance from the player torso/Root position minus the distance of the models primary part which we have as root

			if not playerNearest then
				playerNearest = player

				dist = distanceV.Magnitude -- distance vector magnitude gives us the actual distance
				direction = distanceV.Unit -- direction of the nearest player, SEE DOCUMENTATIOIN FOR UNIT AND MAGNITUDE

			elseif distanceV.Magnitude < dist then -- If the player is closer than the set nearest player then ''replace'' the player

				playerNearest = player -- resets to new player
				dist = distanceV.Magnitude
				direction = distanceV.Unit

			end
		end
	
	end
	
	return playerNearest, dist, direction -- function so return which playa and his distance and direction
end

-- Another call from the runService class that runs every "physics frame", Which I think is like the updateBefore in unity
runService.Heartbeat:Connect(function() -- lua thing essentially this odd function call thing is just an anonymous function meaning it will execute every heartbeat
	local playerNearest, distance, direction = findNearestPlaya()
	-- if the distance is within range of the wanted distance
	if playerNearest  then
		if distance <=wantedDistance and distance >= stopDistance then

			humanoid:Move(direction) -- moves in the direction of the playa
		else 
			humanoid:Move(Vector3.new()) -- 

		end
	end


end)
