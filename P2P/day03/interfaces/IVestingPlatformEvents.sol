// SPDX-License-Identifier: MIT

pragma solidity 0.8.17;

interface IVestingPlatformEvents {
    /**
     * @notice Emited when a vesting has been created
     */
    event NewVesting(
        address indexed beneficiary,
        uint256 indexed index,
        uint64 startTimestamp,
        uint64 endTimestamp
    );

    /**
     * @notice Emited when a vesting has been fully or partially claimed
     */
    event ClaimVesting(
        address indexed beneficiary, uint256 indexed index, uint256 amount
    );
}